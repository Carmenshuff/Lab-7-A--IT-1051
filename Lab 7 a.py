# Name: Carmen Huff
# Course: IT-1051 - Introduction to Programming
# Lab: Lab 7

# Problem 1 - Coffee Shop Ordering Program

total = 0.00
another_item = "yes"

while another_item.lower() == "yes":

    order = input("What would you like to order? ")

    if order.lower() == "coffee":
        price = 3.00
        print("Price: $3.00")
        total += price

    elif order.lower() == "latte":
        price = 4.50
        print("Price: $4.50")
        total += price

    elif order.lower() == "cappuccino":
        price = 4.00
        print("Price: $4.00")
        total += price

    elif order.lower() == "tea":
        price = 2.50
        print("Price: $2.50")
        total += price

    else:
        print("Sorry, that item is not on our menu.")

    another_item = input("Would you like to order another item? ")

print("\nTotal Order Amount: $" + format(total, ".2f"))
print("Thank you for your order!")
