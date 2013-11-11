import MySQLdb as mdb
db=mdb.connect("localhost","root","","pgreg2013")

a=open("dddetails.txt",'r')
a=a.read().split('\n')
with db:
	cur=db.cursor()
	for i in a:
		if i:
			i=i.split(',')
			date='-'.join(i[3].split('/')[::-1])
			print date
		#	cur.execute("insert into dddetails(application_no,amount,bank,branch_payable,dddate,dd_no) value('"+i[0]+"','"+i[1]+"','"+i[4]+"','"+i[5]+"','"+date+"','"+i[2]+"');")
			cur.execute("insert into dddetails1(application_no,amount,bank,branch_payable,dddate,dd_no) value('"+i[0]+"','"+i[1]+"','"+i[4]+"','"+i[5]+"','"+date+"','"+i[2]+"');")
#			cur.execute("insert into ;")
