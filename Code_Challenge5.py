# Create an X shape out of " * "

# fixed
for x in range (5):
    for y in range (5):
        if x + y == 5 - 1 or x - y == 0: # Hindi ko maintindihan.
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()
# Dynamic
n = int(input("Input number of size: "))
for x in range (n):
    for y in range (n):
        if x + y == n - 1 or x - y == 0:
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()