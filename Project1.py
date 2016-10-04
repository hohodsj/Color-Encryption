#!/usr/bin/python
import sys
from colored import fg, bg, attr

print ("Type something")
line = sys.stdin.readline()
wordlist = list(line)
word = "X"
total=0
temp=0
ctr=0
colorctr=0
colorList=[]

for x in range(0,len(wordlist)):
    if wordlist[x] != ' ' and wordlist[x] != '\n':
        if wordlist[x].lower() == 'a':
            temp=1
        if wordlist[x].lower() == 'b':
            temp=10
        if wordlist[x].lower() == 'c':
            temp=20
        if wordlist[x].lower() == 'd':
            temp=20
        if wordlist[x].lower() == 'e':
            temp=30
        if wordlist[x].lower() == 'f':
            temp=40
        if wordlist[x].lower() == 'g':
            temp=50
        if wordlist[x].lower() == 'h':
            temp=60
        if wordlist[x].lower() == 'i':
            temp=70
        if wordlist[x].lower() == 'j':
            temp=80
        if wordlist[x].lower() == 'k':
            temp=90
        if wordlist[x].lower() == 'l':
            temp=100
        if wordlist[x].lower() == 'm':
            temp=110
        if wordlist[x].lower() == 'n':
            temp=120
        if wordlist[x].lower() == 'o':
            temp=130
        if wordlist[x].lower() == 'p':
            temp=140
        if wordlist[x].lower() == 'q':
            temp=150
        if wordlist[x].lower() == 'r':
            temp=160
        if wordlist[x].lower() == 's':
            temp=170
        if wordlist[x].lower() == 't':
            temp=180
        if wordlist[x].lower() == 'u':
            temp=190
        if wordlist[x].lower() == 'v':
            temp=200
        if wordlist[x].lower() == 'w':
            temp=210
        if wordlist[x].lower() == 'x':
            temp=225
        if wordlist[x].lower() == 'y':
            temp=240
        if wordlist[x].lower() == 'z':
            temp=255
        total = total+temp
        ctr=ctr+1

    else:
        total = int(total/ctr)
        colorList.insert(x,total)
        ctr=0
        total = 0



line = line.strip()
wordlist = list(line)

for x in range(0,len(wordlist)):
    if wordlist[x] == " ":
        print(" ",end=''),
        colorctr=colorctr+1
    elif wordlist[x].isalpha():
        color=colorList[colorctr]
        print ('{}{}{}{}'.format(fg(color),bg(color), word, attr("reset")),end=''),

print('')






