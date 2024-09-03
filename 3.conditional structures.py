###1###
zander_limit = float(input('enter the zender length(cm): '))
if zander_limit >=42:
    print('Take it home with you')
else :
    throwlimit = 42-zander_limit
    print(f'release the fish back into the lake,because{throwlimit} centimeters below the size limit')

###2###

cabin_class = input('enter your cabin class:  ')
if cabin_class == 'LUX':
    print('LUX: upper-deck cabin with a balcony')
elif cabin_class == 'A':
    print('A: above the car deck, equipped with a window.')
elif cabin_class == 'B':
    print('B: windowless cabin above the car deck.')
elif cabin_class == 'C':
    print('C: windowless cabin below the car deck.')
else:
    print('Invalid cabin class')

###3###

gender = input('enter your gender(male/female):  ')
hemoglobin_value = float(input('enter your hemoglobinvalue(g/l):  '))
if gender == 'female':
    if hemoglobin_value < 117:
        print('your hemoglobin value  is low')
    elif 117<=hemoglobin_value<=155:
        print('your hemoglobin value is nomal')
    else:
        print('your hemoglobin value is high')
if gender == 'male':
    if hemoglobin_value<134:
        print('your hemoglobin value is low')
    elif 134<=hemoglobin_value<=167:
        print('your hemoglobin value is normal')
    else:
        print('your hemoglobin value is high')

###4###

year = int(input('enter a year: '))
if year%4 == 0:
    print('the year is a leap year')
if year%100 != 0 and year%400 ==0:
    print('the year is a leap year')
else:
    print('it is not a leap year')