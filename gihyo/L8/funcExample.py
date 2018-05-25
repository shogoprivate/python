#coding:utf-8

## Import the module
import funcModule
#from funcModule import * #i = func(5)
#impor funcModule as f    #i = f.func(5)
import turtle 
import kameTool

## Call the function
i = funcModule.func(5)
print(i)


## Edit the module
fileEdit = open("funcModule.py",'w')
fileEdit.write("def func(v):\n")
fileEdit.write("\ti = v*3\n")
fileEdit.write("\treturn i")
fileEdit.flush()
fileEdit.close()


## Reload the module
reload(funcModule)
i = funcModule.func(5)
print(i)


## Edit the module
fileEdit = open("funcModule.py",'w')
fileEdit.write("def func(v):\n")
fileEdit.write("\ti = v+3\n")
fileEdit.write("\treturn i")
fileEdit.flush()
fileEdit.close()


## Call the other function
kame = turtle.Turtle()
kameTool.centerCircle(kame, 50)
