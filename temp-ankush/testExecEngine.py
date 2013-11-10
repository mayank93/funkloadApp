"""
    Module that provides various test interfaces to the web2py app
"""
import subprocess
import os
import Utilities as u

# Global vars

def sanityCheck():
    """ Sanity Check function """
    responseDict = {        }
    
    # Do stuff
    os.chdir('./sanity')
    p = subprocess.Popen(['fl-run-test','test_Sanity.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err, out = p.communicate() 
    length = len(out.split('\n'))

    #print out.split('\n')[length-2]
    if "FAILED" in out.split('\n')[length-2] :
        u.printError('Sanity testing failed...')
        responseDict['status'] = False
    else :
        u.printSuccess('Sanity testing passed...')
        responseDict['status'] = True
    
    os.chdir('..')
    return responseDict

def functionalTest(url_list):
    """ Functional Test function """
    u.printInfo('Initiating Functional Testing...')
    responseDict = {}
    #url_list = ['http://localhost/index.html','http://localhost/inde.html']
    count = 0;
    # Do stuff
    os.chdir('./sanity')
    
    for url in url_list:
        p = subprocess.Popen(['fl-run-test','test_Sanity.py','--url='+url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        err, out = p.communicate() 
        length = len(out.split('\n'))
        if not "FAILED" in out.split('\n')[length-2] :
            responseDict[url]=True
            count = count + 1
        else :
            responseDict[url]=False
    os.chdir('..')
    u.printInfo(str(count) +' out of ' + str(len(url_list)) +' links reachable..') 
    return responseDict


def stressTest():
    """ Stress Test function """
    responseDict = {        }
    
    # Do stuff
    os.chdir('./stress')
    p = subprocess.Popen(['fl-run-test','test_Stress.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err, out = p.communicate() 
    length = len(out.split('\n'))

    #print out.split('\n')[length-2]
    if "FAILED" in out.split('\n')[length-2] :
        u.printError('URL not reachable...')
        u.printError('Stress testing aborted...')
        responseDict['status'] = False
    else :
        u.printSuccess('URL reachable...')
        u.printInfo('Stress testing initiated...')
        p = subprocess.Popen(['fl-run-bench','test_Stress.py','Stress.test_stress'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.communicate()
        #out,err = p.communicate()
        #print out.split('\n')
        p = subprocess.Popen(['fl-build-report','--html','stress-bench.xml'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = p.communicate()

        #returnVal = p.communicate()

        # get the path of the generated report...
        path = out.split('\n')[1]
        u.printInfo('Report stored at '+path)
        responseDict['status'] = True
        responseDict['path'] = path
    
    os.chdir('..')
    return responseDict
