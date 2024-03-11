"""username = input("username: ")
password = input("password: ")

if username == "admin" and password == "admin":
 print("successfully login")
else:
 print("wrong username or password")"""
 
try: 
    int1 = int(input("Enter integer 1: "))
    int2 = int(input("Enter integer 2: "))
    sum = int1 + int2
    print(sum)
except ValueError:
    print("please enter a valid integer")