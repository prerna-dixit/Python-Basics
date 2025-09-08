#print only integers from a list
custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']
for item in custom_list:
    if type(item)==int:
        print(item)