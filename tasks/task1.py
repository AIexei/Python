from modules.text_statistics import *

def task1():
    print("Text statistics\n\n")
    text = ""

    while True:
        print("1. Enter text")
        print("2. Open from file")
        print("3. Go to menu")

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
        elif user_selection == 3:
            return
        else:
            print("Incorrect input\n\n")

    print()
    list = text_to_list(text)

    while True:
        print("1) How much words is repeated ?")
        print("2) The average number of words in sentence")
        print("3) The median number of words in sentence")
        print("4) Top K most repeated N-grams")
        print("5) Exit")

        try:
            user_selection = int(input())
        except ValueError:
            print("Incorrect input\n\n")
            continue

        if user_selection == 1:
            print(reps_of_words(list))
        elif user_selection == 2:
            print(average_count_of_words(list))
        elif user_selection == 3:
            print(median_count_of_words(list))
        elif user_selection == 4:
            k = 0
            n = 0
            while True:
                try:
                    print("Enter K, N:")
                    k = int(input())
                    n = int(input())
                    break
                except ValueError:
                    print("Incorrect input\n\n")
                    continue

            print(top_grams(list, k, n))
        elif user_selection == 5:
            return
        else:
            print("Incorrect input\n\n")

    print("\n")