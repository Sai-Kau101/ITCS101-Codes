#Conditional Statements (if, else)
#Getpass (hide password)

import getpass

username = "user67"
password = "skibidisigma67"

u = input("Enter Username --> ")
p = getpass.getpass("Enter Password --> ")

if username == u and password == p :
	print("Access Granted!")
else:
	print("Access Denied, Incorrect Username or Password")