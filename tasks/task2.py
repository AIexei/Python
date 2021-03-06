from modules.sorting import *
import time

def task2():
    print("Sorting\n\n")
    list = []

    while True:
        print("1. Enter array")
        print("2. Open from file")
        print("3. Go to menu")

        try:
            user_selection = int(input())
        except ValueError:
            print("Incorrect input\n\n")
            continue

        if user_selection == 1:
            print("Enter array:")
            string = input()

            try:
                list = [int(i) for i in string.split(" ")]
                break
            except ValueError:
                print("Incorrect input\n\n")

        elif user_selection == 2:
            print("Enter file name: ")
            file_name = input()

            try:
                with open(file_name) as file:
                    for line in file:
                        temp = [int(i) for i in line.split(" ")]
                        list.extend(temp)
                break
            except FileNotFoundError:
                print("File not found\n\n")
            except ValueError:
                print("Incorrect input\n\n")
        elif user_selection == 3:
            return
        else:
            print("Incorrect input\n\n")


    print("\nList: ")
    print(list)

    print("\n\nQuick sort\n")
    start = time.clock()
    result = quick_sort(list)
    print("Execution time: %.5f s" % (time.clock()-start))
    print(result)

    print("\n\nMerge sort\n")
    start = time.clock()
    result = merge_sort(list)
    print("Execution time: %.5f s" % (time.clock()-start))
    print(result)

    print("\n\nRadix sort\n")
    start = time.clock()
    result = radix_sort(list)
    print("Execution time: %.5f s" % (time.clock()-start))
    print(result)
