###1###

user= input('enter your name: ')
print("Hello,"+ user)

###2###

rds=float(input("enter a number:"))
area=3.14*rds**2
print(f"if your rds is: {rds}, the area is : {area}")

###3###

length = float(input('enter the length of a rectangle: '))
width = float(input('enter the width of a rectangle: '))
C= (length+width)*2
a= length*width
print(f'the C is:{C}, the AREA is :{a}')

###4###

number1 = int(input('enter the first number: '))
number2 = int(input('enter the second number: '))
number3 = int(input('enter the third number: '))
sum = number1+number2+number3
product = number1*number2*number3
average = (number1+number2+number3)/3
print(f'the sum is {sum}, the product is {product}, the average is {average}')

# ###5###

talent = float(input('enter the talent :'))
pound = float(input('enter the pound: '))
lot = float(input('enter the lot'))
talent1 = 20*32*13.3*talent
pound1 = 32*13.3*pound
lot1 = 13.3*lot
sum = talent1+pound1+lot1
kilogram = int(sum/1000)
gram = float(sum%1000)
print(f'The weight in modern units:{kilogram} kilograms and {gram:.2f} grams.')

###6####

import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
print(num1,num2,num3)

num4 = random.randint(1, 6)
num5 = random.randint(1, 6)
num6 = random.randint(1, 6)
num7 = random.randint(1, 6)
print(num4,num5,num6,num7)

