#coding:utf-8

while True:
    height = raw_input("身長(cm)は?:")
    if len(height) == 0:
        continue
    height = float(height)
    if height < 4:
        print("身長をcm単位で入力してください．")
        continue
    else:
        break

while True:
    weight = raw_input("体重(kg)は?:")
    if len(weight) == 0:
        continue
    weight = float(weight)
    break

bmi = weight / pow(height/100, 2)

### string format
print("BMI値は%0.1f" % bmi)

if bmi < 18.5:
    print("少し痩せすぎです．")
elif 18.5 <= bmi < 25.0:
    print("標準的な体型です．")
elif 25.0 <= bmi < 30.0:
    print("少し太っています．")
else:
    print("高度の肥満です．")

