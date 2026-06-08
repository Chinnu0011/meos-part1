#python loops
#for loop
ports = [22,80,443,21]
for port in ports:
    print(f"the ports are {port}")

usernames = ["admin", "hello", "david", "hellogpt", "hellomeo", "helloclaude"]
for user in usernames:
    if user == "hellomeo":
        print(f"the account {user} is found")
#status code:
code = [200, 403, 404, 500]
for status in code:
    if status == 404:
        print(f"the status code is {status}")
    else:
        print(f"the status code is not 404, it is {status}")