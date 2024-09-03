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
#
# count = int(input("enter number"))
# count1 = 0
# while count1<count:
#     print('count is',count1)
#     count1=count1+1
# else:
#     print('bye')
#
#
# count = int(input('enter how many numbers you want count: '))
# showed = 0
# while showed < count:
#     print('the numbers is: ',showed)
#     showed+=1
#
# command = input('enter a comand: ')
# while command != 'stop':
#     print('do the comand:',command)
#     command = input('enter a comand: ')
# print('you enter a stop')
#
#
# import random
# roll_times=0
# while True:
#     dice1=random.randint(1,6)
#     dice2=random.randint(1,6)
#     roll_times=roll_times+1
#     if dice1==6 and dice2==6:
#         print('you got it,the rolled times is:',roll_times,'times')
#         break
#
# import random
# num=random.randint(1,3)
# num1=0
# while True:
#     num1 += 1
#     user_input = int(input('enter a number: '))
#     if user_input==num:
#         print('that is right')
#         print('times is ', num1)
#         break
#     else:
#         print('guess another number')
#
# 列表计数从0开始正数，倒数从-1开始


names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

# print(names[3]) #3意思是正数第四个，从0开始
# print(names[1])
# print(names[-2]) #-2就是倒数第二个
# print(names[1:3]) #1:3就是从第1-3的范围，但不打印3，也就是打印1-2
# print(names[2:]) #2：就是从2到最后
# print(names) #name 打印所有变量

# print(len(names)) 指的是列表中的个数
#
# append添加内容，如果有列表，则从最后添加，打印的是列表,一次只能添加一个
# insert嵌入内容，可以在指定的位置加入内容，而不是在最后增加（从0开始计数，占坑位置，），打印的是列表
# index查找位置，去查找列表中你所需要的内容在第几个,index是一个定义，打印的也是这个定义
# extend 增加列表，在后面直接加，而apend加入更多内容会出现[1, 2, 3, 4, 5, [6, 7]]，多一个括号：子列表情况
#                             extend加入用[],可以继续在总列表添加，而不是子列表情况
# names = []
#
# name = input("Enter the next name or quit by pressing Enter: ")
# while name!="":
#     names.append(name)
#     name = input("Enter the next name or quit by pressing Enter: ")
#
# print(names)

# names = ["Viivi","Ahmed", "Pekka", "Olga", "Mary"]
#
# fx='Pekka'in names
# print(fx)
# names = []
#
# name = input("Enter the first name or quit by pressing Enter: ")
# while name!="":
#     names.append(name)
#     name = input("Enter the next name or quit by pressing Enter: ")
#
# for g in names:
#     print(f"Hello, {g}!")
# Initialize an empty list to store the numbers
numbers = []

# Ask the user to enter numbers until they input an empty string
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    # If the input is an empty string, break the loop
    if user_input == "":
        break

    # Convert the input to a float and add it to the list
    numbers.append(float(user_input))

# Sort the numbers in descending order
numbers.sort(reverse=True)

# Get the top 5 greatest numbers
top_five_numbers = numbers[:5]

# Print the top 5 greatest numbers
print("The five greatest numbers are:", top_five_numbers)

