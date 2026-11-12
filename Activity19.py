# while loop
is_big = True

while is_big == True:
    is_big = bool(input("Is the house big? "))
    
    if is_big == True:
        print("Yes, the house is big.")
        continue
    else:
        break