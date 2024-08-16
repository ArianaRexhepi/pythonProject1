class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name}, and I am  {self.age} yeard old")

person1 = Person("John", 25)
person2 = Person("Alice", 30)

person1.greet()
person2.greet()

