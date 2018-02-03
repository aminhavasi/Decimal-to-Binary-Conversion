# Decimal-to-Binary-Conversion
This repository explains the concept of conversion of decimal to binary numbers

# Algorithm to convert whole numbers to binary
  Step 1. Input a number, num
	Step 2. Repeat steps 3, 4, and 5 until num = 0
	Step 3. Calculate remainder of num relative to 2 and store in rem
	Step 4. Binary = binary + (str)rem
	Step 5. Integer divide the num
	Step 6. Stop
  
# Algorithm to convert floats into binary
  Step 1: start
  Step 2: Multiply the number by a power of 2 big enough to convert that fractional number into whole number
	Step 3: Convert this new whole number into binary(above algo)
	Step 4: Divide(shift right) the resultant by the power of 2 multiplied earlier
  Step 5: Stop
