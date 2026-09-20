"""
import math

print(math.pi)
print(math.sqrt(49))
print(math.pow(2,3))

from math import sqrt
print(sqrt(49))

import random 
import string
print(random.randint(100,200))
random_letter=random.choice(string.ascii_letters)
print(random_letter)
small_letter=random.choice(string.ascii_lowercase)
print(small_letter)
capital_letter=random.choice(string.ascii_uppercase)
print(capital_letter)

num=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(num))
print(random.sample(num,k=5))

#try out secret module

import datetime 
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.date.today()-datetime.timedelta(1))    #Yesterdat
print(datetime.date.today()+datetime.timedelta(1))    #Tomorrow

from datetime import datetime
now=datetime.now()
current_time=now.time()
print(current_time)

#try out random days between specific days

import sys
print(sys.platform)
print(sys.version)
import os
print(os.getcwd())
print(os.listdir())


import datetime as dt
print(dt.datetime.now())

import requesst()
"""

import requests
url=requests.get('https://jsonplaceholder.typicode.com/users/1')
print(url.json())