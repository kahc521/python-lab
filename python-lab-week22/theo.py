my_string = input("Enter a string: ")
l = len(my_string)
if  l < 4:
    print("invalid entry")
else:
    print("valid entry")
    
    
try:
    # Take two integers as input from the user
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    # Calculate the sum of the two integers
    sum_of_integers = num1 + num2

    # Print the sum
    print("The sum of", num1, "and", num2, "is:", sum_of_integers)

except ValueError:
    print("Invalid input! Please enter integers only.")    