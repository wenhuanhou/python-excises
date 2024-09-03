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
# 编写一个游戏，让计算机绘制一个介于 1 和 10 之间的随机整数。用户尝试猜测数字，直到猜出正确的数字。每次猜测后，
# 程序都会打印出一个文本：Too high、Too Low 或 Correct。请注意，计算机不得更改两次猜测之间的数字。
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
# 编写一个程序，要求用户提供用户名和密码。如果其中一个或两个不正确，程序将要求用户再次输入用户名和密码。这种情况会一直持续，
# 直到登录信息正确或输入了五次错误的凭据。
# 如果信息正确，程序将打印出 Welcome。在五次尝试失败后，程序将打印出 Access denied。
# 正确的用户名是 python 和 password rules。
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
# 编写一个程序，询问用户要生成多少个随机点，然后使用上述方法计算(taogongshi) pi 的近似值。最后，程序将 pi 的近似值打印给用户。
# （请注意，通过测试一个点是否满足不等式 x^2+y^2<1，很容易测试它是否落在圆 A 内。
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








