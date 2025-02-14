def StringCompare(str1,str2):
    str1= str1.lower()
    str2= str2.lower()

    dict1={}
    for char in str1:
        dict1[char] = dict1.get(char,0)+1

    dict2={}
    for char in str2:
        if dict1.get(char,0)>0:
            dict1[char] -= 1
        else:
            print("No, string2 can't be built from string1")
            return
    print("Yes, string2 can be built from string1")


str1 = input("Enter string1: ")
str2 = input("Enter string2: ")


StringCompare(str1, str2)