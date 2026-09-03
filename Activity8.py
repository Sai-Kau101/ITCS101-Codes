hobbies = " " #blank string

hb = input("What are your hobbies? -->")
hobbies += hb + ", "

hb = input("Any other hobby? -->")
hobbies += hb + " ,and "

hb = input("A hobby you really like? -->")
hobbies += hb

print("My hobbies are: ", hobbies)