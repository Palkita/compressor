
import subprocess as sb
import os
path=input("Enter path of the folder  : ")
ls = os.listdir(path)
for i in ls:
    s=path+"\\"+i
    d=s+".zip"
    cmd="powershell Compress-Archive "+s+" "+d
    sb.call(cmd,shell=True)

print("Sucessfully compressed .")