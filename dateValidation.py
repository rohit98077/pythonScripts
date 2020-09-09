def validate_date(dateStr):
	dateLst=dateStr.split('/')
	d,m,y=int(dateLst[0]),int(dateLst[1]),int(dateLst[2])
	flag,isleap=1,0
	if y%100 !=0 and y%4==0 or y%400==0:
		isleap=1
	if y<1850 or y>2050 or m<1 or m>12 or d<1 or d>31:
		flag=0
	elif m==2:
		if d==31 or d==30 or d==29 and not isleap:
			flag=0
	elif m==4 or m==6 or m==9 or m==11:
		if d==31:
			flag=0
	if flag:
		print('valid Date')
	else:
		print('invalid Date')


date_=input('Enter date as dd/mm/yyyy :')
while date_:
	validate_date(date_)
	print('Enter another date to check or just hit enter to leave.')
	date_=input()

