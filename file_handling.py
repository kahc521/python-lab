''' 
f= open("test.txt" , 'w')    # 'w' , 'a' , 'r'
f.write("#this is the first line\n")
f.write("*this is the second line")
f.close
'''
try:
    with open("test1.txt" , 'r') as f:
        f.readline
    f.close
except:
    print("please check the file name")

