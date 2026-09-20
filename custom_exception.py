"""
class Custom_Exception(Exception):
    pass   #to do nothing 
def check_number(num):
    if num<0:
        raise Custom_Exception("Not allowed negative numbers")
    return num
try:
    result=check_number(-7)
except Custom_Exception as e:
    print(e)
else:
    print(result)

class NameTooShortError(Exception):
    pass
name=input("Enter The User Name: ")
try:
    if len(name)<8:
        raise NameTooShortError("Name must be greater than 8 letters")
except NameTooShortError as e:
    print(e)
"""

class InsufficientBalanceError(Exception):
    pass
amount=int(input("Enter the amount: "))
available=5000
try:
    if amount>available:
        raise InsufficientBalanceError("Insufficient Balance")
except InsufficientBalanceError as e:
    print(e)
else:
    print("Transaction Succesful")

