# Task 4: Method Chaining
# Create class User
# Methods:
# register()
# login()
# greet()
# Rule:
# Each method must return self
# Example:
# user = User()

# user.login().greet().register()
# Expected Output:
# logined
# enjoy everyone
# registered

class User:
    def login(self):
        print("logined")
        return self    

    def greet(self):
        print("enjoy everyone")
        return self    

    def register(self):
        print("registered")
        return self  


# Method chaining
user = User()
user.login().greet().register()