customer_name=input("Enter Customer Name: ")
food_item_name=input("Enter Food Item: ")
quantity=int(input("Enter Quantity: "))
price_per_item=float(input("Enter Price Per Item: "))
delivery_distance=float(input("Enter Delivery Distance(charged ₹10/km): "))

print("Customer Name is: ",customer_name)
print("Ordered Food Item is: ",food_item_name)
print("Quantity of Food is : ",quantity)
print("Price Per Item : ",price_per_item)
print("Delivery Distence : ",delivery_distance)

data1=delivery_distance
data2=10
data3=data1*data2
print(("DElivery Cachrge: ₹"),data3)

data4=quantity
data5=price_per_item
data6=data4*data5
data7=data6+data3
print(("Total cost: ₹"),data7)


