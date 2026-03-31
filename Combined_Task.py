# Task 5: Combined Task (Real-Time)
# Build a Mini User System
# Features:
# Encapsulation for user data
# Inheritance:
# User
# Student
# Faculty
# Method overriding for greet()
# Method chaining for:
# user.login().greet().register()
# Bonus:
# Add class variable:
# users_count
# Increment on each object creation


class User:
    users_count = 0     

    def __init__(self, name, pwd):
        self.__name = name       
        self.__pwd  = pwd     
        User.users_count += 1  

    #  getters (controlled access)
    def get_name(self):
        return self.__name

    # chainable methods (return self) 
    def login(self):
        print(f"{self.__name} logged in.")
        return self

    def register(self):
        print(f"{self.__name} registered.")
        return self

    # overridable greet
    def greet(self):
        print("Welcome User")
        return self


# Inheritance + Overriding 
class Student(User):
    def greet(self):         
        print("Welcome Student")
        return self               


class Faculty(User):
    def greet(self):   
        print("Welcome Faculty")
        return self              


#  Demo
print("*" * 40)
s = Student("Alice", "stu123")
f = Faculty("Bob",   "fac456")

print(f"\nTotal users created: {User.users_count}")

print("\n--- Student chain ---")
s.login().greet().register()

print("\n--- Faculty chain ---")
f.login().greet().register()

print("\n--- Polymorphism loop ---")
for user in [s, f]:
    user.greet()

print("\n--- Encapsulation check ---")
print(f"Name via getter : {s.get_name()}")
# print(s.__name)   # AttributeError: private cannot access directly

print(f"\nFinal users_count: {User.users_count}")