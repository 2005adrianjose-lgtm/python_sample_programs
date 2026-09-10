"""
if ondition:
   code to be executed
elif ondition:
    code to be executed
else:
    code to be executed    
"""
"""
num=int(input("Enter a number: "))
if num>=0:
    print("Positive number")
else:
    print("Negative number")
"""
"""
vowelcheker=input("Enter a cahrecter")
if vowelcheker in "aeiouAEIOU":
    print("Enter char is a vowel")
else:
    print("Entered char is a consonent")
    
"""
"""
num=int(input("Enter a number"))
if num%2==0:
    print("Number is even")
else:
    print("Nunber is odd")    
"""
#age <=13 child , age <18 teenager , age<60 adult , else->senior citizen
"""
age=int(input("Enter your age: "))
if age<=13:
    print("child")
elif age<18:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior citizon")
"""
"""
num=int(input("Enter a number: "))
if num>=0:
    if num%2==0:
        print("Number is positive and even")
    else:
        print("Number is positive and odd")
else:
    print("Negative number")
""" 
#check whether given num is 3 digit or not

#for and while are entry controller loops

"""

for variable in sequence: 
    code to be executed 

#Using range function
for variable in range(start,stop,step):
    code to be executed

start=default value is 0
stop=number -1
step=default value is 1 for positive numbers and for negative numbers we need to assign

#syntax for while loop:
initialization 
while condition:
    code to be executed
    updation
"""

"""
word=input("Enter a word: ")
for letter in word:
    print(letter)
"""
"""
for item in [1,2,3,4,5]:
    print(item)
"""
"""
for element in range(11):
    print(element)
"""
"""
for element in range(5,15):
    print(element)
"""
"""
for element in range(10,26,5):
    print(element)
"""
"""
for item in range(10,0,-1):
    print(item)
"""
"""
for item in range(17,3,-3):
    print(item)
"""
"""
multiple=int(input("Enter a number: "))
for item in range(1,11):
    #print(multiple,"*",item,"=",item*multiple)
    print(f"{multiple} * {item} = {item*multiple}")
 """   
 """
value=1
iterations=int(input("Enter the number of iterations: "))
while value<=iterations:
    print(value)
    value+=1
"""