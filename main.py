from tasks.task1 import *
from tasks.task2 import *
from tasks.task3 import *
from tasks.task4 import *

while True:
    print("\nChange task:")
    print("1. Text statistics")
    print("2. Sorting")
    print("3. Unique items")
    print("4. Generator of Fibonacci numbers")
    print("0. Exit\n")

    try:
        user_selection = int(input())
    except ValueError:
        print("Incorrect input\n\n")
        continue
    if user_selection == 1:
        task1()
    elif user_selection == 2:
        task2()
    elif user_selection == 3:
        task3()
    elif user_selection == 4:
        task4()
    elif user_selection == 0:
        break
    else:
        print("Incorrect input")