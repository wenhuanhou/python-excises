##1###

import random
user_roll=input('how many dices you want to roll: ')
amount=0
for n in range(int(user_roll)):
    random_dice=random.randint(1,6)
    print(random_dice)
    amount=random_dice+1

print('the amount is:',amount)

##2###

numbers=[]
user_input=0
while user_input!="":
    user_input = input('enter your number or press enter to quit: ')
    if user_input=="":
        break
    numbers.append(float(user_input))
numbers.sort(reverse=True)
five_numbers = numbers[:5]

print('The five greatest numbers are:', five_numbers)

##3###

user_input = int(input("enter a integer: "))
prime_num = True
if user_input <= 1:
    prime_num = False
else:
    for i in range(2, user_input):
        if user_input % i == 0:
            prime_num = False
            break
if prime_num:
    print(f"{user_input} is a prime.")
else:
    print(f"{user_input} is not a prime.")

###4###

cities = []

for i in range(5):
    city = input("enter a city name: ")
    cities.append(city)

print("The city is :")
for city in cities:
    print(city)



