""" 
def function_name(perameters):
    code to be executed
"""

#user difined funtion without parameter
"""
def welcome():
    print("Welcome Adrian")

welcome()
welcome()
"""

#user difined funtion with parameter
"""
def greeting(username,userage):
    print(f"Welcome {username},you are {userage} years old")

greeting("AdriaN",21)
"""
"""
def addition(num1,num2):
    return num1+num2

num1=int(input("Enter the first number: "))
num2=int(input("Enter the secont number: "))

print(addition(num1,num2))
"""

#Positional argument
"""
def book_ticket(moviename,customername,seats,ticketprice):
    totalprice=seats*ticketprice
    return f"{customername} booked {seats} tickets for {moviename}. Total amount: {totalprice}"

print(book_ticket("Avengers","Adrian",6,150)) #only works if u give the required amout of arguments and wont work with less of more arguments
"""
#Keyword argument
"""
def customer_details(customername,customerage,city):
    print(f"{customername} is {customerage} years old.and he is from {city}")
customer_details(customerage=21,customername="Adrian",city="Amaravila")
"""

#Default argument
"""
def booking_status(customername="John",status="confirmed",screen="screen1"):
    print(f"{customername}'s booking status is {status}. The screen allocated is {screen}")

booking_status()

booking_status("Bob")
booking_status("Jerry","pending")
booking_status("Tom","pending","screen2")
"""

#Multiple arguments
"""
def calculate_bill(*ticketprices):   
    print(f"ticketprices: {ticketprices}")
    
calculate_bill(150,200,230,220,100)
"""
#Built in function
"""
print(len("Lenny"))
print(sum([5,6,7,8,9]))
print(min([6,5,4,3,2]))
print(max([1,2,3,4,5]))
print(sorted([3,5,1,8,9,2,6]))
print(sorted([3,5,1,8,9,2,6],reverse=True))
"""

           #LEGB rule
"""
def student_details():
    name="Adrian"
    print("student name: ", name)
student_details()
"""
#Global variable
"""
college_name="vazhichal emmanual college"
def display():
    print("collage name: ",college_name)
display()
"""

#Enclosing
"""
def department():
    department_name="Cs"
    def student():
        print("Deparyment name: ",department_name)
    student()
department()
"""
"""
tax=50#global variable
def shopping():
    discount=100#enclosing variasble
    def bill():
        amount=2500
        total_amount=amount-discount+tax
        print("Total smount is: ",total_amount)
    bill()
shopping()
"""
"""
#Recursive function
def factorial(number):
    if number==1:  #base case
        return 1
    else:  #recursive case
        return number*factorial(number-1)
num=int(input("Enter a number: "))
print(factorial(num))
"""
"""
#working :-
6*factorial(5)
6*5*factorial(4)
6*5*4*factorial(3)
6*5*4*3*factorial(2)
6*5*4*3*2*factorial(1)
"""

#Lamda function (anonymous funtion)
#Lambda arguments:expression  syntax
"""
def add(num1,num2):
    return num1+num2
print(add(2,3))

add=lambda a,b:a+b
print(add(5,6))

square=lambda num:num*num
print(square(5))

multiply=lambda a,b:a*b
print(multiply(5,6))

cube=lambda x:x**3
print(cube(3))

is_odd=lambda x:x%2!=0
print(is odd(7))
"""