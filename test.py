def check_number(str):
    for i in range(len(str)):
        if str[i].isdigit() is False:
            return False
    return True


str = "Akiff"
if check_number(str):
    print(str + " is an integer ")
else:
    print(str + " is a string ")

str1 = "123"
if check_number(str1):
    print(str1 + " is an integer ")
else:
    print(str1 + " is a string ")
