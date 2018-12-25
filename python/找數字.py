#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
maxx = int(input('the max num was:'))
guess = random.randint(1,maxx)# 告訴我們隨機產生整數亂數
print('Let\'s play some game')
answer =int(input("Enter a number: "),10)#讀取十進位的整數
a = 5 #有五次機會

while (answer != guess):
    print('you are wrong!!')
    if(answer<guess):
        print('Bigger')
    else:
        print('Smaller')
    a-=1
    if(a ==0):
        print('no chance left')
        break
    else:
        print('you have '+str(a)+' chance left')
        answer =int(input("Enter a number: "),10)
if(answer ==guess):
    print('congradulation')
