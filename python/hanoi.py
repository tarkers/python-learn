#hanoi
num=0
def hanoi(n,x,y,z):
    global num
    num+=1
    if n ==1:
        print(x,'--->',z)
    else:
         hanoi(n-1,x,z,y)#將前n-1個盤子移動到Y上
         print(x,'--->',z) #將最底下的盒子X移動到Z上
         hanoi(n-1,y,x,z)#將y上的n-1盤子移動到Z上

n= int(input('enter the number:'))
hanoi(n,'X','Y','Z')
print('you should move at least %d times' %num)
