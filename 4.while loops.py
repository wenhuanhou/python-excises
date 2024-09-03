##1###

num=1
while num<=1000:
    num += 1
    if num % 3 == 0:
        print('the numbers is:', num)

##2###

while True:
    numbers=float(input('enter a number(inch): '))
    if numbers<0:
        print('Negative number is invalid')
        break
    centimeters=numbers*2.54
    print(numbers,'inches is',centimeters,'cm')
import random


maxnum=None
minnum=None


while True:
    user_input = input('enter a number: ')
    if user_input=="":
        print('get out')
        break
    user_input=float(user_input)
    if maxnum==None or user_input > maxnum:
        maxnum=user_input
    if minnum==None or user_input < minnum:
        minnum = user_input
print('the max number is: ',maxnum)
print('the min number is: ',minnum)

##4###

import random
num=random.randint(1,10)
while True:
    user_input = int(input('enter a number: '))
    if user_input==num:
        print('Correct')
        break
    if user_input>num:
        print('Too high')
    if user_input<num:
        print('Too low')
###5###

username = 'python'
password = 'rules'
num=0
while True:

    user_input_name=input('enter your username: ')
    user_input_password=input('enter your password: ')
    num += 1
    user_name=username
    user_password=password
    if user_input_name!=username or user_input_password!=password:
        print ('Try it again')
    if num==5:
        print('Access denied')
        break

    if user_input_name == username or user_input_password == password:
        print('Welcome')
        break

###6###

import random
Amount_randompoint=int(input('enter a number: '))
i=0
circle_randompoint=0
while i<=Amount_randompoint:
    num1=random.uniform(-1,1)
    num2=random.uniform(-1,1)

    if num1**2+num2**2<1:
        circle_randompoint += 1
    value=(4*circle_randompoint)/Amount_randompoint

    i+=1
print('the approximation of pi is ',value)








