#!/usr/bin/python
import sys
from colored import fg, bg, attr

print ("Type something, press enter to quit the program")
line = sys.stdin.readline()
word = "X"

while 1:
    wordlist = list(line)
    total=0
    temp=0
    ctr=0
    colorctr=0
    colorList=[]
    

    def colornum( letter ):
        num = ord(letter.lower()) - 97
        return num*10

    def avecolor(total,ctr):
        total = int (total/ctr)
        return total


    for x in range(0,len(wordlist)):
        if wordlist[x].isalpha():
            temp = colornum(wordlist[x])
            total = total+temp+1
            ctr=ctr+1

        else :
            if not(wordlist[x].isalpha()) and not(wordlist[x-1].isalpha()):
                continue
            else:
                total = avecolor(total,ctr)
                colorList.insert(x,total)
                ctr=0
                total = 0



    line = line.strip()
    wordlist = list(line)
    if(line == "-quit"):
        break
    if not line:break

    for x in range(0,len(wordlist)):
        if wordlist[x] == " " or wordlist[x] == "+" or wordlist[x] =="=":
            print(wordlist[x],end=''),
            colorctr=colorctr+1
        elif wordlist[x].isalpha():
            color=colorList[colorctr]
            print ('{}{}{}{}'.format(fg(color),bg(color), word, attr("reset")),end=''),
        else:
            print(wordlist[x],end=''),
#colorctr=colorctr+1



    print('')
    line = ''
    colorList=[]
    line = sys.stdin.readline()




