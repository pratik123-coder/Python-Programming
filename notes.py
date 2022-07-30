'''-------------------First Program-------------------'''
print("Hello world")

'''
-------------------Adding Comments In A Program-------------------
Comments - They are certain lines in a program that you dont want to be exectued.
'''
import time
from turtle import pencolor
time.sleep(2)
#Change the time according to your preference (This is a Comment)
print("This will be pri
nted after 2 seconds") 

'''-------------------Modules in Python-------------------
A set of codes in which the codes are already written by someone and you can use
it without knowing what the code actually does.
'''
import math #Here Math is a MODULE
a=math.pow(2,3)
print(a)

'''-------------------Data Types, Variables And Operators-------------------
Variable- Name given to a memory location in program
Rules For Writing Variable Names
1) It should only contain alphabets, digits and underscores
2) It can only start with a alphabet or a underscore
3) No spaces are allowed inbetween variable names
'''
a=30    #Here a,b and c are variables which store value and return it when called
b="Hey"
c=71.22

'''
Data Types - Primary data types are 
1)Integers (all natural numbers)
2)Float (all real numbers)
3)Strings ( characters that are included betwen '' or " ")
4)Boolean (binary data type which has 2 values "True" and "False")
'''
a=231           #Integer Data Type
b=12.23         #Float Data Type
c='Hey people'  #String Data Type ('' "")
d=True          #Boolean Data Type

'''
Operators In Python
Arithematic Operators => +,-,*,/
Assigmenet Operators => =,+=,-=
Comparision Operators => ==,>,<,!= (Used in Logic Building In a Program (VIMP))
Logical Operators =>  or and,and not
'''
a=56
b=34
#this is a assginment operator 

print("a+b=",a+b)    
print("a-b=",a-b)
print("a*b=",a*b)    #these are arithmatic operators
print("a/b=",a/b)

#This is comparision operator where we compare between a and b
if a==b:
    print("both number are equal")
elif a<b:
    print("a is smaller than b")
elif a>b:
    print("a is bigger than b")
else:
    print("Both are not equal")\

#This is Logical Operator
a=50    
b=75
print(a==b and a<b)
print(a!=b or a>b)
print(not(a==b))

'''
Type Casing In Python 
'''
a=12
b="Hey People"
c=12.23
d=True

print(type(a))
print(type(b)) 
print(type(c))      #This will show what data type they belong to 
print(type(d)) 

#typecasting
a=23
b="23"
print(a==b)
c=int(b)    #typecasted b varible to a integer type
print(a==c)
#simiarly you can type cast it to any type such as bool, none, string and interger

'''
User Input Statements
'''
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("The sum of a and b is: ",a+b)
print("The difference of a and b is: ",a-b)
print("The multiplication of a and b is: ",a*b)
print("The division of a and b is: ",a/b)

'''-------------------Strings In Python-------------------
It is a Data Type in Python. 
Strings in python are combination/ sequence of characters in between quotes.
'''
a="Hello World"
b='A Place'
print(a)
print(b)    
print(a+b)

'''
String Slicing
A String in Python can be sliced for getting a part of the string. 

Lets Consider a string = "Hello"
 H  e   l   l   o   --> STRING NAME
 0  1   2   3   4   --> STRING Number From Left To Right
-5 -4  -3  -2  -1   --> STRING Number From Right To Left
The Index in a string starts from O to (Length -1). For instance we have to write
the code in the following way.
st = name[int start : int end]
'''
a="Hello"
print(a[0:2])

'''
Gaps in a Slicing 
If there is a string a = "Hello" and if i want to print 'H' 'l' 'o'
they are at index number '0' '2' '4'
to get gaps st = name[int start : int end : int gaps]
'''
a="Hello"
print(a[0:5:2])

'''
"myStr.endswith" and "myStr.startswith" fuction
myStr.endswith   --> If a certain string ends with certain characters then it 
returns true
myStr.startswith --> If a certain string starts with certain characters then it 
returns true
myStr.count      --> Counts the number of occurances of acharacters in a string
myStr.capitalize --> Capitalizes the first word of the string
myStr.find       --> Finds the index number of first letter of the word.
myStr.replace    --> Replaces the old word with a new word.
'''
a="asjkdhfjkexyz"
b="Hello World"
c="what are you doing"
print(a.endswith("xyz"))

print(a.startswith("ask"))

print(b.count('l'))

print(b.capitalize())

print(c.find("are"))

print(c.replace("what","how"))
'''
Escape Sequence In Python

Are characters in which we input 2 characters but it reads as a Single character
/n  --> New Line
/t  --> Tab Space
'''
myStr="My Name is Pratik"
print(myStr)
myStr1="My Name\n is Pratik"
print(myStr1)
myStr2="My Name\t is Pratik"
print(myStr2)
'''
----------------Lists And Tuples----------------

Lists--> Python lists are containers to store a set of values of any data type 
list1=["apple","suresh", "rohan", 7, 8, False, True]
It can store numbers, strings, boolean and any datatype 
'''
myLst=["hey", False , "suresh", 1,2]
print(myLst)

'''
Lists Indexing
let suppose a list is l1=[7,9,"pratik"]
then    7 is at 0 or -3 index
        9 is at 1 or -2 index
 "pratik" is at 2 or -1 index
 The indexing principle is just same as that of a string
'''
l1=[2,4,6,"Hey People"]
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
'''To print specific range of values from list
myLst[starting index : ending index : gaps in between (if required)]
'''
myLst1=["hey", "wassup",2,3,4,5,6,7]
print(myLst1[0:4])
print(myLst1[0:5:2])
print(myLst1[0:7:3])

'''
Lists Methords

list.sort()    --> Updates the List in ascending manner if all contents are int
list.reverse() --> Updates the List in reverse manner
list.append()  --> Adds a Specific content in the list given in the paranthesis
                   at the last
list.
 
'''
