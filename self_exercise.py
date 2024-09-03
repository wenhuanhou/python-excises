# while True:
#     rounds = int(input("How many greetings: "))
#     finished_rounds = 0
#     while finished_rounds<rounds:
#         print("Good morning")
#         finished_rounds = finished_rounds + 1
#     if rounds == 0:
#         print('get out')
#         break
# greeting = int(input('enter how many times: '))
# counter = 0
# while counter<greeting:
#     print('good morning',counter)
#     counter+=1

# count = int(input("enter number"))
# count1 = 0
# while count1<count:
#     print('count is',count1)
#     count1=count1+1
# else:
#     print('bye')

#
# count = int(input('enter how many numbers you want count: '))
# showed = 0
# while showed < count:
#     print('the numbers is: ',showed)
#     showed+=1

# command = input('enter a comand: ')
# while command != 'stop':
#     print('do the comand:',command)
#     command = input('enter a comand: ')
# print('you enter a stop')


# import random
# roll_times=0
# while True:
#     dice1=random.randint(1,6)
#     dice2=random.randint(1,6)
#     roll_times=roll_times+1
#     if dice1==6 and dice2==6:
#         print('you got it,the rolled times is:',roll_times,'times')
#         break

import random
num=random.randint(1,3)
num1=0
while True:
    num1 += 1
    user_input = int(input('enter a number: '))
    if user_input==num:
        print('that is right')
        print('times is ', num1)
        break
    else:
        print('guess another number')













