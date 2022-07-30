lst=[]
a=int(input("Enter first number "))
lst.append(a)

b=int(input("Enter the second number "))
print("this is the list you gave",lst)

e=int(input("Enter the number you want to check for"))

if (e in lst==True):
    print("Yes the number is present")
else:
    print("NO the number is not present")
for i in range(0,a):
    if i==3:
        print("_", end="")
        lst.append(i)
# lst.insert(0,34)
# if (99 in lst==True):
#     print("99 is present in the list")
# else:
#     print("99 is not in the list")