class Student:
    # school_name = "Digital School" #class variable

    def __init__(self, name, age, course): #Instance variables
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Bob", 15, "Python")
student2 = Student("John", 20, "Java")

print(student1.course)
print(student2.course)