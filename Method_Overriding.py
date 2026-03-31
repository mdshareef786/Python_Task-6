# Task 3: Method Overriding
# Use same User, Student, Faculty
# Requirement:
# Override greet() method
# Parent:
# def greet():
#     print("Welcome User")
# Student:
# print("Welcome Student")
# Faculty:
# print("Welcome Faculty")
# Expected:
# student.greet() → Welcome Student
# faculty.greet() → Welcome Faculty

# Parent
class User:
    def greet(self):
        print("Welcome User")


# Child classes override greet()
class Student(User):
    def greet(self):            
        print("Welcome Student")


class Faculty(User):
    def greet(self):          
        print("Welcome Faculty")


# Demo
u = User()
s = Student()
f = Faculty()

u.greet() 
s.greet()  
f.greet()  

# Polymorphism — same call, different result
print("\n--- Loop demo (polymorphism) ---")
for person in [u, s, f]:
    person.greet()

# Accessing the parent version from inside the child
print("\n--- Calling parent greet() via super() ---")
class Student2(User):
    def greet(self):
        super().greet()      
        print("Welcome Student")

Student2().greet()