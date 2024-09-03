###1###
import random

def roll_dice():
    return random.randint(1, 6)
roll = 0

while roll != 6:
    roll = roll_dice()
    print(f"The result is: {roll}")

###2###
import random

def roll_dice(sides):
    return random.randint(1, sides)


sides = int(input("enter a number of a dice side: "))
roll = 0


while roll != sides:
    roll = roll_dice(sides)
    print(f"The result is : {roll}")

###3###

def gallons_to_liters(gallons):
    return gallons * 3.78541

while True:

    gallons = float(input("a volume in gallons(or quit with a negative number)："))

    if gallons < 0:
        print("program stopped")
        break

    liters = gallons_to_liters(gallons)

    print(f"{gallons} gallons is {liters:.2f} liters。")

###4###
def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def main():
    my_list = [1, 2, 3, 4, 5]

    result = sum_of_list(my_list)

    print(f"list {my_list} is: {result}")

if __name__ == "__main__":
    main()

###5###

def remove_odd_numbers(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    return even_numbers

def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    filtered_list = remove_odd_numbers(original_list)


    print(f"The original list is : {original_list}")
    print(f"The filtered list is: {filtered_list}")

###6###
import math

def calculate_unit_price(diameter_cm, price_euros):
    radius_cm = diameter_cm / 2.0
    area_sqm = math.pi * (radius_cm / 100.0) ** 2
    unit_price = price_euros / area_sqm
    return unit_price

def main():

    diameter1 = float(input("enter the first pizza diameter(cm): "))
    price1 = float(input("enter the first pizza price(euros): "))


    diameter2 = float(input("enter the first pizza diameter(cm):"))
    price2 = float(input("enter the first pizza price(euros): "))


    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    print(f"The first unit price of the pizza per square meter: {unit_price1:.2f} euros")
    print(f"The second unit price of the pizza per square meter: {unit_price2:.2f} euros")

    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money。")
    elif unit_price1 > unit_price2:
        print("The second pizza provides better value for money。")
    else:
        print("Both of them have the same value for money。")


if __name__ == "__main__":
    main()

