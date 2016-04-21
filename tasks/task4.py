from modules.fibo import fibo

print("Generator of Fibonacci numbers\n\n")
number = 0

while True:
    print("1. Enter number")
    print("2. Open from file")

    try:
        user_selection = int(input())
    except ValueError:
        print("Incorrect input\n\n")
        continue

    if user_selection == 1:
        print("Enter number: ")
        try:
            number = int(input())
            break
        except ValueError:
            print("Incorrect input\n\n")
    elif user_selection == 2:
        print("Enter file name: ")
        file_name = input()

        try:
            with open(file_name) as file:
                number = int(file.read())
            break
        except FileNotFoundError:
            print("File not found\n\n")
        except ValueError:
            print("Incorrect input\n\n")
    else:
        print("Incorrect input\n\n")


print()

for item in fibo(number):
    print(item)


