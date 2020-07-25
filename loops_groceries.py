groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]

quantity = int(input("How many of each item did you buy?"))

for item in groceries:

    print(f"{item[0]:<20} ${item[1] * quantity:.2f}")
 #   print(sum(item[1])

# for item, price in groceries():
#     print(item, price)

# sum1 = 0
# for item in groceries:
#     sum1 += int(item)
# print("Sum of list = ", sum1)