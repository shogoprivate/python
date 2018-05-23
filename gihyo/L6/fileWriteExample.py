#coding:utf-8

#---------------------------
# write mode 
#---------------------------
testFile = open("test1.txt", 'w')

testFile.write("Hello!\nPython\n")

testFile.flush()
testFile.close()


#---------------------------
# read mode 
#---------------------------
testFile = open("test1.txt", 'r')

string = testFile.readline()
print("1行目は:"+string)        
# This "string" includes the control character 
# "strip()" method is needed

testFile.close()


testFile = open("test1.txt", 'r')

stringList = testFile.readlines()
for i in stringList:
# for i in testFile: でも可
    num = stringList.index(i)
    i = i.strip()
    print(str(num+1)+"行目は:"+i)

testFile.close()


#---------------------------
# Example 
#---------------------------
data = ["1,2,3\n","4,5,6\n","7,8,9\n"]
testFile = open("test2.txt", 'w')

testFile.writelines(data)

testFile.flush()
testFile.close()

testFile = open("test2.txt", 'r')

for i in testFile:
    i = i.strip()
    print(i)

testFile.close()

print("tab変換")

testFile = open("test2.txt", 'r')

for i in testFile:
    i = i.strip().split(',')
    i = '\t'.join(i)
    print(i)

testFile.close()
