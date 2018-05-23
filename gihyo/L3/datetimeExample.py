#coding:utf-8

import datetime

day = datetime.date(2018, 5, 23)
print(day)

kyo = datetime.date.today()
print("Today is "+str(kyo))

yobi = kyo.weekday()
if (yobi==0):
    yobi = "Mon"
elif (yobi==1):
    yobi = "Tue"
elif (yobi==2):
    yobi = "Wed"
elif (yobi==3):
    yobi = "Thr"
elif (yobi==4):
    yobi = "Fri"
elif (yobi==5):
    yobi = "Sat"
else:
    yobi = "Sun"
print("Day of the week is "+yobi)

ima = datetime.datetime.now()
print("Now is "+str(ima))

year2000 = datetime.date(2000, 1, 1)
delta = kyo - year2000
print("Days from 2000 to today is "+str(delta.days))
