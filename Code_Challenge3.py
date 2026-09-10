#Code Challenge 3
#Global Freight Calculator

#Inputs

sender_name = input("Sender Name:")
item_type = input("Type of Item:")
is_fragile = input("Is the item FRAGILE? True or False?")
weight = float(input("Weight (kg):"))
distance = float(input("Distance (km):"))
is_express = input("Is the item a RUSHED order? True or False?")
is_international = input("Is the item an INTERNATIONAL order? True or False?")

#Calculations

base_cost = (weight * 2.50) + (distance * 0.15)

#Outputs

print("Your order... \n Sender:", sender_name, "\n Type of Item:", item_type)

if weight <= 2 and distance <= 100 and is_express == "False" and is_international == "False":
	print("Free Shipping")
elif is_international == "True" and is_express == "True":
	print("Total Fee: $", (base_cost * 1.40) + 50)
elif is_express == "True" or is_international == "True" and weight > 20:
	print("Total Fee: $", (base_cost * 1.20) + 25)
elif weight > 30 or distance > 1000:
	print("Total Fee: $", base_cost + 30)
else:
	print("Total Fee: $", base_cost)