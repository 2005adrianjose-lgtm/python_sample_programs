#object:- is an entity that is having state behaviour and identity 
#eg: pen-> identity is its name/ state: colour,brand,model/ behaviour: it can write,draw,etc.
#Class:- is a group of similer objects or user defined datatype
#There are 4 basic principles or pillers in oops
#1.Inheritance
#2.Polymorphism
#3.Abstraction
#4.Encapsulation
"""
class Student: #use pascal for class name
    def display(self): #self is importent
        print("I am a student")
student_object=Student() #object creation
student_object.display()
"""
#constructor:- special type of method in python. Mainly used for initializing an object. It will be automatically called when an object is created.

class Employee:
    def __init__(self): #init is the constructor
        print("Default constructor is called")
employee_object=Employee()

