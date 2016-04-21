from modules.unique_items import *

store = UniqueItems()

def console():
    list = input("store >>> ").split(' ')

    if list[0] != 'exit':
        if hasattr(store, list[0]):
            try:
                args = []
                for item in list[1:]:
                    if item != '':
                        args.append(int(item))

                getattr(store, list[0])(args)
            except ValueError:
                print("Error: incorrect input\n")
        else:
            print("Error: function " + list[0] + " not found")

        print()
        console()


print("Unique items store\n\n")

while True:
    print("1. Use store")
    print("2. Go to menu")

    try:
        user_selection = int(input())
    except ValueError:
        print("Incorrect input\n\n")
        continue

    if user_selection == 1:
        console()
    elif user_selection == 2:
        break
    else:
        print("Incorrect input\n\n")