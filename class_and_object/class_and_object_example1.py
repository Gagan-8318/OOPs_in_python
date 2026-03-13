class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating object
s1 = Student("Gagan", 22)

s1.show()