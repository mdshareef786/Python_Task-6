# Task 2: Inheritance (User → Student, Faculty)
# Create parent class User
# Parent Class:
# register()
# login()
# Child Classes:
# Student
# student_greet() → print "Hello Student"
# Faculty
# faculty_greet() → print "Hello Faculty"
# TempFaculty (Multilevel)
# Inherit from Faculty
# tempFaculty_greet() → print "Hello Temp Faculty"
# Practice:
# Call all methods using objects
# Show:
# Child can access parent methods
# Parent cannot access child methods

# Parent class
class User:
    def register(self):
        print("User registered.")

    def login(self):
        print("User logged in.")


# Single inheritance
class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


# Multilevel inheritance
class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# Demo
print("---- Student ----")
s = Student()
s.register()          
s.login()             
s.student_greet()   

print("\n---- Faculty ----")
f = Faculty()
f.register()     
f.login()       
f.faculty_greet()    

print("\n---- TempFaculty ----")
tf = TempFaculty()
tf.register()    
tf.login()         
tf.faculty_greet()  
tf.tempFaculty_greet() 

print("\n---- Parent cannot reach child---- ")
u = User()
u.register()

print("u.student_greet() would raise AttributeError")