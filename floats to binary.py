num = float(input("Enter a number between 0 and 1: "))
p = 0
binary = ''

while ((2**p)*num)%1 != 0:
    p += 1

num2 = int((2**p)*num)

if num2 == 0:
    binary = '0'
    
while num2 > 0:
    binary = str(num2%2) + binary
    num2 = num2//2

for i in range (p - len(binary)):
    binary = '0' + binary

print('Binary equivalent: ', binary[0:-p], '.', binary[-p:])
