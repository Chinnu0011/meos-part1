#Day4 of python mastery
'''
print("*** TARGET RECON TOOL ***")
target = input("Enter Target IP:")
port = int(input("Enter port number:"))
print(f"scanning ...... target ip - {target} on port {port}")
'''
'''
 🧪 Practice Task
Write a program called login_sim.py:

Ask user for username
Ask user for password
Ask user for age (convert to int)
Print all 3 using f-string in this format:

[*] User: meo | Age: 21 | Password length: 8

Hint: len(password) gives you the length.

Save it. Push to GitHub. Show me the output. '''

print("LOGIN PYTHON")
username = input("Enter your name:")
password = input("Enter secret code:")

age = int(input("enter your age:"))
print(f" [*] User: {username} | Age: {age} |  password length: {len(password)}")
