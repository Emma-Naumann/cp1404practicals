"""
CP1404 - Practical 1
Shop Calculator
"""

total_price = 0
number_items = int(input("Number of items: "))
while number_items < 0:
    print("Invalid number of items!")
    number_items = int(input("Number of items: "))
for i in range(number_items):
    item_price = float(input("Price of item: $"))
    total_price += item_price
if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount
print(f"Total price for {number_items} items is ${total_price:.2f}")
