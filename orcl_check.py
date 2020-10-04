import cx_Oracle
con=cx_Oracle.connect("system/12345678@localhost:1521")
# con=cx_Oracle.connect('system','12345678','MYSERVICE')
cur=con.cursor()
cur.execute("select 'Hello World' from dual")
res=cur.fetchall()
print(res)

# cur.execute('DROP TABLE emp')
# createQuery='''create table emp(eid number,ename varchar2(10), sal number(*,2),age number(*,0), primary key (eid))'''
# cur.execute(createQuery)
# cur.execute("insert into emp values(100,'rohan', 80000,30)")
# cur.execute("insert into emp values(101,'rahul', 90000,30)")

cur.execute('select * from emp')
res=cur.fetchall()
for r in res:
	print(r) 
con.commit() 
if cur:
	cur.close() 
con.close()
