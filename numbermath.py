#Asks user: "Enter a port number:"
#Converts input to int
#Checks if the port is even or odd using modulo (print the result)
#Prints the port squared using **
#Prints the result of port // 1000 (tells you which "thousand range" the port is in — like 8080 → 8)

port = int(input("Enter port number:"))
if port % 2 == 0:
   print("given port is even ")
else:
   print("port is odd") 
squred = port ** 2
print(f"the power of given port number is {squred}")
result = port // 1000
print(f"the result is {result}")
