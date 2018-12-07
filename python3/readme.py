# -*- coding: UTF-8 -*-
import re

strline =""
with open('C:\Python35\README.txt','r') as f:
    for line in f.readlines():
        if("Copyright (c)"in line):
            strline+=line[14:]
        if("2012" in line):
            strline+=line




print(strline)

stre = re.compile('[a-zA-Z]|,|\.')
alphaBet = stre.findall(strline)
for i in alphaBet:
    strline = strline.replace(i,'')


strline = strline.replace('-',' ')
print(strline)


strline = strline.split()

print(strline)

hap = 0;
for i in range(0,len(strline)):
    print(int(strline[i]))

    hap = hap + int(strline[i])

print(hap)
