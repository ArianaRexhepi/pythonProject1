class Myclass:
    def __init__(self):
        self.__private_variable = "This is a private variable"

    def private_method(self):
        print("This is a private method")

my_class = Myclass()

print(my_class.__private_variable)
my_class.private_method()