#coding:utf-8

import dice

val = int(raw_input("4, 6, 8, 12, 20のどれで勝負しますか? :"))

cpu = dice.Dice(val).shoot()
you = dice.Dice(val).shoot()

print("CPU:"+str(cpu))
print("You:"+str(you))

if cpu>you:
    print("残念．あなたの負けです．")
elif cpu<you:
    print("おめでとう．あなたの勝ちです!")
else:
    print("引き分けです．")
