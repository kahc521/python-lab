username = "admin"
password = "admin"

Entered_username=input("Please enter your username: ")
Entered_password=input("Please enter your password: ")

if Entered_username == username and Entered_password == password:
    print("successfully login")
else:
    print("wrong username or password")
