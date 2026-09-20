"""
print("statement 1")
print("statement 2")
print("statement 3")
try:
    value1=10
    value2=0
    value3=value1/value2  #zero division error
except ZeroDivisionError:
    print("denominator cant be zero")
print("statement 4")
print("statement 5")
"""

#try except else
"""
numerator=int(input("Enter the numenator"))
dinominator=int(input("Enter the denominator"))
try:
    quotient=numerator/dinominator
except ZeroDivisionError:
    print("denominator cant be zero")
else:
    print("quotient")
"""
#type error
"""
try:
    num1=15
    num2="25"
    add=num1+num2
    print(add)
except TypeError:
    print("string cant be added with integer value")
 """  
 #Index Error :- Index out of range 
"""
numbers=[1,2,3,4,5,6,7,8,9,10]
try:
    print(numbers[10])
except IndexError:
    print("index out of range")
"""

#key error-dictionary
"""
book_details={
    "book_id":2,
    "book_name":"atom habits"
}
try:
    print(book_details["book author"])
except KeyError:
    print("key not found")
"""

#Filenotfound
"""
try:
    with open("test_file.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found in directory")
"""
#Import Error
"""
try:
    from math import square
except ImportError as e:
    print(e)
"""

#Attribute Error
"""
try:
    user_value="Welcome"
    print(user_value.add())
except AttributeError as e:
    print(e)
"""  
#Value error
"""
try:
    data=int("Adrian")
except ValueError as e:
    print(e)
"""

#Name error
"""
try:
    print(student)
except NameError as e:
    print(e)
finally:          
    print("executed normally")
"""

#Multiple exception
"""
try:
    data=int("Adrian")
    user_value="Welcome"
    print(user_value.add())
except ValueError as e:
    print(e)
except AttributeError as e:
    print(e)
"""
#Multiple exception using another method

try:
    data=int("Adrian")
    user_value="Welcome"
    print(user_value.add())
except (ValueError,AttributeError) as e:
    print(e)

