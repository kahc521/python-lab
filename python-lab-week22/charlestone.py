

while True:
    zip_code = input("Please enter a zip code: ")
    z_1 = len(zip_code.strip())
    z_2 = zip_code.isdigit()
    if  z_1 == 5 and z_2 == True:
        print(" your entry is valid")
        break
    else:
        print("invalid entry")
        