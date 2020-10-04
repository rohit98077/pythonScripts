def dayOfWeek(dateStr):
	dateLst=dateStr.split('/')
	d,m,y=int(dateLst[0]),int(dateLst[1]),int(dateLst[2])
	j=d
	j+={
		0:0,
		1:31,
		2:31+28,
		3:31+28+31,
		4:31+28+31+30,
		5:31+28+31+30+31,
		6:31+28+31+30+31+30,
		7:31+28+31+30+31+30+31,
		8:31+28+31+30+31+30+31+31,
		9:31+28+31+30+31+30+31+31+30,
		10:31+28+31+30+31+30+31+31+30+31,
		11:31+28+31+30+31+30+31+31+30+31+30
		}[m-1]
	
	if y%100 !=0 and y%4==0 or y%400==0:
		if m>2:
			j+=1
	y-=1
	day=(y+j+y//4-y//100+y//400)%7
	return {
	1:'Monday',
	2:'Tuesday',
	3:'Wednesday',
	4:'Thursday',
	5:'Friday',
	6:'Saturday',
	0:'Sunday',
	}[day]

date=input('Enter date as dd/mm/yyyy :')
while date:
	print(dayOfWeek(date))
	print('Enter another date to check or just hit enter to leave.')
	date=input()