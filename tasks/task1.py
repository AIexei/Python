from modules.text_statistics import *

print("Text statistics\n\n")
list = []

while True:
    print("1) Enter text")
    print("2) Open from file")

    try:
        user_selection = int(input())
    except ValueError:
        print("Incorrect input\n\n")
        continue

    if user_selection == 1:
        print("Enter text: ")
        text = input()

        if text != "":
            break
    elif user_selection == 2:
        print("Enter file name: ")
        file_name = input()

        try:
            with open(file_name) as file:
                text = file.read()
            break
        except FileNotFoundError:
            print("File not found\n\n")


print()

