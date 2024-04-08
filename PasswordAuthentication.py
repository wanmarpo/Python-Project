# Password authentication with a database

import getpass

database = {"Norman" : "123abc", "Bella" : "qwerty135"}
login = True

while True:
    username = input("Enter Your Username : ")
    password = getpass.getpass("Enter Your Password : ")

    if username in database:
        # Username exists in the database
        if password == database[username]:
            break  
        else:
            # Incorrect password
            print("Incorrect password. Please try again.")
            while password != database[username]:
                password = getpass.getpass("Enter Your Password Again :")
            break
    else:
        # Username not found in the database
        print("Username not found. Please try again.")

# Password matches for the given username
print("Login Successful!")