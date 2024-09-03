# ###1###
#
# seasons = ("Winter", "Spring", "Summer", "Autumn")
#
# month = int(input("Enter a number in month（1-12）："))
#
# if month < 1 or month > 12:
#         print("Invalid number，Enter number 1-12。")
# else:
#
#     if month in (12, 1, 2):
#         season = seasons[0]
#     elif month in (3, 4, 5):
#         season = seasons[1]
#     elif month in (6, 7, 8):
#         season = seasons[2]
#     else:
#         season = seasons[3]
#
#     print(f"The month is: {season}")



##2###

# names_set = set()
#
# while True:
#     name = input("Enter your name or press enter to quit :")
#
#     if name == "":
#         break
#
#     if name in names_set:
#             print("Existing name")
#     else:
#             print("new name")
#             names_set.add(name)
#
# print("\nThe names you input are：")
# for name in names_set:
#     print(name)

#
# ###3###
#
def main():
    airports = {}

    while True:
        print("\nchoose a menu:")
        print("1. enter a new airport")
        print("2. airport information")
        print("3. quit")

        choice = input("enter（1, 2 or 3）：")

        if choice == "1":

            icao_code = input("enter an airport ICAO code:").upper()
            airport_name = input("enter the name of the airport:")
            airports[icao_code] = airport_name
            print(f"You add an new airport:{airport_name} ({icao_code})")

        elif choice == "2":

            icao_code = input("enter an airport ICAO code:").upper()
            if icao_code in airports:
                print(f"{icao_code} the airport name is:{airports[icao_code]}")
            else:
                print(f"Not found the ICAO code of the airport {icao_code} .")

        elif choice == "3":

            print("quit")
            break

        else:

            print("Invalid input，enter 1, 2 or 3.")

if __name__ == "__main__":
    main()
