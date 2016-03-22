class UniqueItems(object):
    def __init__(self):
        self.store = set()


    def add(self, items=list()):
        if type(items) is list:
            self.store.update(items)
        else:
            self.store.add(items)


    def remove(self, items=list()):
        if type(items) is list:
            for i in items:
                self.store.remove(i)
        else:
            self.store.remove(items)


    def find(self, items=list()):
        flag = True

        if type(items) is list:
            for i in items:
                if not i in self.store:
                    flag = False

            print(flag)
        else:
            if items in self.store:
                print("True")
            else:
                print("False")


    def clear(self, waste=list()):
        self.store.clear()


    def load(self, waste=list()):
        file_name = input("Enter file name: ")

        try:
            with open(file_name, "r") as file:
                self.clear()

                for line in file:
                    for i in line.split(" "):
                        if i != "":
                            self.add(i)
            print("Store loaded")
        except FileNotFoundError:
            print("File not found")
        except ValueError:
            print("Incorrect input")


    def save(self, waste=list()):
        file_name = input("Enter file name: ")
        print (file_name)
        with open(file_name, "w") as file:
            for item in self.store:
                file.write(str(item))
                file.write(" ")

        print("Store saved")


    def list(self, waste=list()):
        result = sorted(self.store)
        print(result)

