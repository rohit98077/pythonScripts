def date_diff(date1,date2):
	dateLst=date1.split('/')
	d1,m1,y1=int(dateLst[0]),int(dateLst[1]),int(dateLst[2])
	dateLst=date2.split('/')
	d2,m2,y2=int(dateLst[0]),int(dateLst[1]),int(dateLst[2])
	if d2<d1:
		if m2==3:
			if y2%100 !=0 and y2%4==0 or y2%400==0:
				d2+=29
			else:
				d2+=28
		elif m2==5 or m2==7 or m2==10 or m2==12:
			d2+=30
		else:
			d2+=31
		m2-=1
	if m2<m1:
		m2+=12
		y2-=1
	y=y2-y1
	m=m2-m1
	d=d2-d1
	print('Diff of two dates is : '+str(y)+' years '+str(m)+' months '+str(d)+' days')
	return None

date1=input('Enter first date as dd/mm/yyyy :')
date2=input('Enter second date as dd/mm/yyyy :')
while date1 and date2:
	date_diff(date1,date2)
	print('Enter another date pair to check or just hit enter to leave.')
	date1=input()
	date2=input()
