inp = int(input("Enter a decimal number: "))
binary = ''
rem = 0
while(inp!=0):
    rem = inp % 2
    inp = inp // 2
    binary = str(rem) + binary
print("Binary equivalent is: ", binary)
