import sys
import MySQLdb as sql
import time
import atexit
import codeGen
import testExecEngine as TEE
import os
import grabber
import shutil

db = sql.connect("localhost", "root", "root", "funkLoad")
c = db.cursor()
db.autocommit(True)

REP_BASE = "/home/mayank/Desktop/web2pyAdmin/web2py/web2py/applications/FunkLoad/static"

def cleanup():
    print "Cleaning up..."
    db.commit()
    db.close()

atexit.register(cleanup)

def newTest():
    #c = db.cursor()
    c.execute("SELECT * from TestDetails WHERE status = '0';")
    r = c.fetchone()
    if r == None:
        return -1
    return r[0]

def updateStatus(recID, newStatus):
    query = "UPDATE TestDetails SET status='%s' WHERE id='%s';"%(newStatus, recID)
    c.execute(query)
    db.commit()

def updateCol(ID, colName, newVal):
    query = "UPDATE TestDetails SET %s=%s where id=%s"%(colName, newVal, ID)
    c.execute(query)

def startTests(ID):
    query = "SELECT sanityflag, functionalflag, stressflag FROM TestDetails where id = %s;"%(ID,)
    #query = "SELECT * FROM TestDetails where id = %s;"%(ID,)
    c.execute(query)
    r = c.fetchone();
    FLAG_SANITY = False
    FLAG_SPIDER = False
    FLAG_STRESS = False

    if r[0].lower().startswith('t'): FLAG_SANITY = True
    if r[1].lower().startswith('t'): FLAG_SPIDER = True
    if r[2].lower().startswith('t'): FLAG_STRESS = True

    retVal = None

    if FLAG_SANITY: retVal = sanityTest(ID)

    if retVal == True and FLAG_SPIDER == True:
        FLAG_SPIDER = True
    else:
        FLAG_SPIDER = False

    updateCol(ID, 'status', '1')
    #print retVal
    updateVal = 'true' if retVal else 'false'

    query = "UPDATE TestDetails SET sanity='" + updateVal + "' WHERE id = '" + str(ID) + "';"
    #print query
    c.execute(query)

    if FLAG_SPIDER: retVal = spiderTest(ID)

    if FLAG_STRESS: retVal = stressTest(ID)

def sanityTest(ID):
    query = "select url, requestperuser, CycleDuration, CycleUser from TestDetails where id = %s"%(ID,)
    c.execute(query)
    r = c.fetchone()
    print r
    codeGen.createCode(r[0], r[1], r[2], r[3], 'Sanity.conf')
    os.rename('Sanity.conf', 'sanity/Sanity.conf')
    result = TEE.sanityCheck()
    return result['status']

def spiderTest(ID):
    print ID
    query = "select url, requestperuser, CycleDuration, CycleUser from TestDetails where id = %s"%(ID,)
    c.execute(query)
    r = c.fetchone()
    print r
    codeGen.createCode(r[0], r[1], r[2], r[3], 'Sanity.conf')
    os.rename('Sanity.conf', 'sanity/Sanity.conf')
    query = "select url, requestperuser, CycleDuration, CycleUser from TestDetails where id = %s"%(ID,)
    c.execute(query)
    r = c.fetchone()
    print r
    urls = grabber.grabber(r[0])
    urls = list(set(urls))
    #if len(urls) > 15:
        #urls = urls[:15]

    print urls

    retVal = TEE.functionalTest(urls)
    total_urls = len(retVal.keys())
    working_urls = 0
    for i in retVal.keys():
        if retVal[i] == True:
            working_urls += 1
    for i in urls:
        if i not in retVal.keys():
            print i
    print working_urls, '/', total_urls

    print retVal

    ratio = 100 if total_urls == 0 else working_urls*100.0/total_urls

    #query = "UPDATE TestDetails SET functional = '" + ratio + "' where ID = '" + ID + "';";
    query = "UPDATE TestDetails SET functional = '%d' WHERE id = '%s'" % (int(ratio), ID)
    c.execute(query)
    query = "UPDATE TestDetails SET status = 2 WHERE id = '%s'" % (ID, )
    c.execute(query)

    for i in retVal.keys():
        query = "INSERT INTO FunctionalTesting(TestId, Url, Status) values('%s', '%s', '%s')"%(ID, i, retVal[i])
        c.execute(query)

def stressTest(ID):
    #print ID
    query = "select url, requestperuser, CycleDuration, CycleUser from TestDetails where id = %s"%(ID,)
    c.execute(query)
    r = c.fetchone()
    print r
    codeGen.createCode(r[0], r[1], r[2], r[3], 'Sanity.conf')
    os.rename('Sanity.conf', 'sanity/Sanity.conf')
    shutil.copy('sanity/Sanity.conf', 'stress/Stress.conf')
    retVal = TEE.stressTest()
    #print retVal
    path = retVal['path']
    reportPath = path.split(os.path.basename(path))[0]
    print reportPath
    dstPath = REP_BASE + '/' +  str(ID)
    print dstPath
    os.system("cp -r " + reportPath + " " + dstPath)

    query = "UPDATE TestDetails SET status = 3 where ID = %s" % (ID, )
    c.execute(query)


while True:
    print "Executing test-loop"
    nextID = newTest()
    print nextID
    try:
        if nextID != -1:
            startTests(nextID)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        raise
        print "[ERROR] Error encountered while processing query"
        query = "UPDATE TestDetails SET status = '4' where ID = %s" % (nextID, )
        c.execute(query)
    time.sleep(1)
