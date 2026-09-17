name = input("Input your NAME:")
age = int(input("Input your AGE:"))

print("Hi there ", name, " Your age is considered as:")
if age >=1 and age <=5:
	print("Infant")
elif age >=6 and age <=12:
	print("Kid")
elif age >=13 and age <=19:
	print("Teenager")
elif age >=20 and age <=29:
	print("Early Adulthood")
elif age >=30 and age <=48:
	print("Adult")
elif age >=49 and age <=59:
	print("Advance Adulthood")
elif age >=60 and age <=100:
	print("Senior")
elif age >=101 and age <=150:
	print("Immortal, Grabe tibay mo.")
else:
	print("Invalid")