#coding:utf-8

countryCode = {1:"America", 39:"Italia", 86:"China"}

#---------------------------
# check a key
#---------------------------
a = (81 in countryCode)
b = (39 in countryCode)
print("81は"+str(a))
print("36は"+str(b))

#---------------------------
# add a value / rewrite a value
#---------------------------
countryCode[81] = "Japan"
print(countryCode[81])
countryCode[81] = "Nippon"
print(countryCode[81])

#---------------------------
# remove a pair of the key and the value 
#---------------------------
countryCode[1] = "Nippon"
print("Before:"+str(countryCode))
countryCode.pop(1) 
print("After:"+str(countryCode))

