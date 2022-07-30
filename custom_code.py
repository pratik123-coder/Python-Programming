

a=int(input("Enter a Number"))
b=int(input("Enter Another Number"))
c=int(input("Choose What You want To Do \n1.Add \n2.Subtract \n3.Multiply \n4.Divide"))
if(c==1):
    print(a+b)
elif(c==2):
    print(a-b)
elif(c==3):
    print(a*b)
elif(c==4):
    print(a/b)
else:
    print("Enter a valid number")