my_list = ['terraform','aws','linux','devops', 2, 5.6, True, 2, 1 , 1]

#List Methods .append() , .pop(), .clear(), .copy() , change item, len(), extend(), insert(),

print(len(my_list))
my_list.append('houston')
print(my_list)
my_list.pop()
print(my_list)
my_list[0]='Terraform'
print(my_list)
print(my_list[2].upper())
my_list.extend([10,56,78])
print(my_list)
print(dir(list))
my_list.insert(1, 'serge')
print(my_list)