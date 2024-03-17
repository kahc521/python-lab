"""a = input("Username:    ")
b = input("Password:    ")
if a == 'admin' and b ==  'admin':
    print("successfully login")
    
else:
    print("wrong username or password")
"""
email_address = input("Enter your email address: ")
if "@" not in email_address:
    print("Invalid email")
else:
    print("valid email")