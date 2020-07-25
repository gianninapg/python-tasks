numbers = input("Enter a number")
numberList = numbers.split()

print("\n")
print("All entered numbers ", numberList)

# Calculating the sum of all user entered numbers
sum1 = 0
for num in numberList:
    sum1 += int(num)
print("Sum of all entered numbers = ", sum1)