from tasks import *

while True:
    print("\nChange task:")
    print("1. Text statistics")
    print("2. Sorting")
    print("3. Unique items")
    print("4. Generator of Fibonacci numbers\n")

    try:
        user_selection = int(input())
    except ValueError:
        print("Incorrect input\n\n")
        continue

    if user_selection == 1:
        import tasks.task1
    elif user_selection == 2:
        import tasks.task2
    elif user_selection == 3:
        import tasks.task3
    elif user_selection == 4:
        import tasks.task4
    elif user_selection == 0:
        break
    else:
        print("Incorrect input")