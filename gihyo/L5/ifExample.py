#coding:utf-8

import datetime

kyo = datetime.date.today()
yobi = kyo.weekday()

if yobi < 4:
    print("頑張って働こう．")
elif yobi == 4:
    print("ゆっくりやろう．")
else:
    print("休日だー")
