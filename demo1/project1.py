my_string = input("enter a string:  ")
a = len(my_string.strip())

print(f"The string entered is: {a} character")
if  a < 4:
    print("Invalid entry")

elif a > 4:
    print("Valid entry.")