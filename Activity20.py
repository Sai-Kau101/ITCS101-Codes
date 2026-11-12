from getpass import getpass
is_login = False

while is_login == False:
    username = input("Input Username: ")
    password = getpass("Input Password: ")
    
    if username == "Dhan" and password == "123456":
        print("Access Granted")
        is_login = True
    else:
        print("Access Denied")
        is_login = False
    