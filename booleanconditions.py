'''
5. Practice Task
Write a script access_checker.py:

Ask user for username (input)
Ask user for password (input)
Hardcode the correct username as "admin" and password as "Pass123"
If both match → print [*] Login successful: Access level FULL
If username is correct but password is wrong → print [*] Login failed: Incorrect password
If username is wrong → print [*] Login failed: Unknown user '''
#Day 4 of python 
#boolean and conditions
username = input("Enter user name:")
password = input("Enter password:")
#username = "admin"
#pasword = "Pass123"
if username == "admin" and password == "Pass123":
    print("[*] Login successful: Access level FULL")
elif username == "admin":
    print("[*] Login failed: Incorrect password")
else:
    print("[*] Login failed: Unknown user")

   
   