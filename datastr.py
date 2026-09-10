#string- immutable data structure
#list- [] ordered collection , mutable ,allow duplicates can be acceses using indexing
# tuple- () ordered collection , immutable ,allow duplicates can be acceses using indexing
#set- {} unordered collection, mutable, does not allow duplicates, cannot be acceses using index
#dictionary- {key:value}ordered collection, value can be changed, allow duplicate values, can be accesed using key

username="Adrian"

"""
 A  d  r  i  a  n
 0  1  2  3  4  5  Positive Indexing
-6 -5 -4 -3 -2 -1  Negative Indexing
 1  2  3  4  5  6  length

print(username[2])
print(len(username))
print(username[-2])
#Indexing returns a single value and slicing gives a set of string or substring


#Slicing

#syntax:- [start:stop:step]
#start-start default value is 0
#stop -value -1
#step- number of skips (defaultly 1 for positive numbers)
data="Python is a programming language"
print(data[:8])
print(data[2:8])
print(data[2:12:3])
print(data[6:])
print(data[1:10:-2]) #this wont work cuz the first given start number is lesser than given step
print(data[10:1:-2])
print(data[::-2])
print(data[::-1])


#string methods
text="Python is very good"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.startswith("yt"))
print(text.endswith("good"))
text[0]="r"
print(text)
print(id(text))
uppercase=text.upper()
print(id(uppercase))


#List          used to make changes on a list
#crude operation-create, view, update, delete
userdata=["Adrian",21,"TVM"] #create
print(userdata)              #view
userdata.insert(1,"EMC")     #update
userdata.append(2026)
userdata.extend("python")
userdata.append(["eng","hindi","mal"])
print(userdata)
print(userdata[11])
print(userdata[11][0])
userdata.extend(["html","css"])
print(userdata)
userdata[0]="Adrian Jose Wilfred"
print(userdata)
userdata.remove("TVM")
print(userdata)
userdata.reverse()
print(userdata)"""

#Tuple- immutable data structure
"""
tuple1=(1,2,3,4,5)
print(tuple1)

#nested tuple

tuple2=("adrian","jose","wilfred",(6,7,8))
print(tuple2)

#tuple unpacking
person=("adrian",21,"tvm")
name,age,place=person
print(name)

num=(10,20,30,40,50)
a,b,*c=num
print(c)
print(a)
print(b)

num1=(10,20,30,40,50)
f,*g,h=num1
print(f)
print(g)
print(h)

num2=(10,20,20,30,40,40,50)
print(num2.count(20))
print(num2.index(30))
print(num2[2])

name=input("enter a string: ")
count=0
for char in name:
    count+=1
print("the count is: ",count)

user_input=input("enter a string: ")
for letter in user_input:
    if user_input.count(letter)==1:
        print("first non-repeting charecter is: ",letter)
        break
else:
        print("no non-repeting charecters")

#repeating charecter index, seconf non repeating charecter, without using count function
"""
#====================================================================

#Set- {},unordered collection of mutable ones, no duplicate

student1={"eng","hindi","mal"}
student2={"eng","hindi","mal"}
student3={"python","urudu"}
student1.add("C")
#studnet1.add("kannada","marathi") #only one argument just like append
#print(student1)
student1.update(["c++","java"])
"""print(student1)
student1.pop()
print(student1)"""
#student1.remove("arabic")
#print(student1)
student1.discard("arabic")
#print(student1)

#union

"""
print(student1)
print(student2)
print(student1.union(student2))
print(student1|student2)
"""
#intersection
"""
print(student1.intersection(student2))
print(student1|student2)
"""
#difference

"""
print(student1.difference(student2))
print(student1-student2)
"""
#symetric difference

"""
print(student1.symmetric_difference(student2))
"""

#subset superset disjoint

#frozenset- immutable 
"""
fs1=frozenset("Adrian")
fs2=frozenset([1,2,3,4,2,3,4])
print(fs1)
print(fs2)
"""
#dictionary

student={
    "name":"Adrian",
    "age":21,
    "place":"TVM",
}

print(student)
print(student["name"])

info=dict(city="tvm",state="kerala") 
print(info.keys())
print(info.values())
#print(info["mark"])


student.pop("age")
print(student)

for key,value in student.items():
    if key=="name":
        print(key,value)

employee={
    "emp1":{
        "name":"Adrian",
        "age":21
    },
    "emp2":{
        "name":"John",
        "age":20
    },
    "emp3":{
    "name":"Alex",
    "age":22
    }
}

print(employee["emp3"]["age"])

