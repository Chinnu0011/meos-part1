#DAY 2
payload = " GET /admin HTTP/1.1 "
print(payload.strip())
print(payload.strip().upper())
print(payload.strip().lower())
print(payload.strip().replace("GET", "POST"))
print(payload.strip().find("admin"))
print(payload.strip().count("T"))
print(payload.strip().split(" "))
print(len(payload))


# Day 2 - String Methods Practice
# Meo's Payload Analyzer

raw_input = "  POST /login?user=admin&pass=1234 HTTP/1.1  "

# Task 1: Strip the spaces
# Task 2: Make it all uppercase
# Task 3: Replace "admin" with "hacker"
# Task 4: Find the index of "login"
# Task 5: Count how many "/" exist
# Task 6: Split it by spaces into a list
# Task 7: Print the total length
print(raw_input.strip())
print(raw_input.strip().upper())
print(raw_input.strip().replace("admin", "hacker"))
print(raw_input.strip().find("login"))
print(raw_input.count("/"))
print(raw_input.strip().split(" "))
print(len(raw_input))