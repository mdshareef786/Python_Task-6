# OOP Practice Tasks (Python)

# Task 1: Encapsulation (User Class)
# Create a class User with proper encapsulation
# Requirements:
# Make variables private
# __user_name
# __pwd
# Create:
# set_user(user_name, pwd)
# get_user() → return username only (hide password)
# Add:
# register() → print username
# login() → print login message

# Expected Output:
# Registering user: john
# Logging in: john

class User:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name  # password intentionally hidden

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")


# --- Usage ---
user = User()
user.set_user("john", "secret123")
user.register()
user.login()