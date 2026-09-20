""" 
    Operators
1.Arithemetic operator
2.Assighment operator
3.Logical operator
4.Comparison operator
5.Bitwise operator
6.Membership operator
7.Identity operator
"""
"""
print("Arithmetic operator")
price_per_phone=20000
quantity=5
total_price=price_per_phone*quantity
average_price=total_price/quantity
gst_added=200
final_price=total_price+gst_added
discount_amount=1000
final_price=final_price-discount_amount
number_of_person=3
remaining_price=final_price%number_of_person
floor_division=final_price//7

print("Price per phone is: ",price_per_phone)
print("Quantity is: ",quantity)
print("Total price is: ",total_price)
print("Average price is: ",price_per_phone)
print("GST added is: ",gst_added)
print("Discount amount of phone is: ",discount_amount)
print("Final price of phone is: ",final_price)
print("Floor division is: ",floor_division)
"""

#Assignment operator
"""score=100
score+=50
score-=20
score*=3
print(score)"""

"""
#Logical operator

and- both the conditions must be true 
or- any of the conditions must be true 
not- opposite of that conditions 
"""
"""
username="Adrian"
password="adrian54321"
entered_username=input("Enter the username: ")
entered_password=input("Enter the password: ")
if username==entered_username and password==entered_password:
    print("Logged in successfully")
else:
    print("Invalid login")  
"""

#or operator

"""
day=input("Enter a day")
if day=="saterday" or day=="sunday":
    print("Holiday")
else:
    print("Working day")  

"""

logged_in=False
if not logged_in:
    print("Login succesful, Welcome user")
else:
    print("Please login") 

"""
#Membership operator checks whether an element is present or not keyword "in" and "notin"

movies=["Black panther","Iron man","Spider man"]
movie=input("Enter a movie")
if movie in movies:
    print("movie avilable")
else:
    print("movie not avilavle")
"""
"""
    #notin
employees=["Bob","Cat","Him"]
employee_name=input("Enter the employee name:")
if employee_name not in employees:
        print("Asses denied")
else:
        print("Asses granted")    
"""
#identity operator-checks wether memmory location is same or not
"""
value1=35
value2=35
print(value1 is value2)
print(value1==value2)

list1=[35,33,32,31]
list2=[35,33,32,31]
print(list1 is list2)
print(list1==list2)
"""
"""a=5
b=3
print(a & b)

#0 1 0 1
#0 0 1 1
#0 0 0 1 

print(a | b)

#0 1 0 1
#0 0 1 1
#0 1 1 1

print(a ^ b)

#0 1 0 1
#0 0 1 1
#0 1 1 0

print(~a)

print(5<<1) #5*2^1
print(5<<2)

print(5>>1) #5%2^1
print(5>>2) 
"""
