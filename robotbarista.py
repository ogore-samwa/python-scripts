print("I am Ogore " + "and I am learning Python! " + "It's a great programming language.")

#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python programming concepts!!

#Let's build robot baristas that can take orders, make coffee, and serve customers! We'll use classes to create our robot baristas and functions to handle the different tasks they can performe

print("Welcome to networkChuck's Coffee Shop! We have a variety of drinks to choose from, including coffee, tea, and smoothies.")

customer_name = input("What is your name? ")

print("Hello, " + customer_name + "! What would you like to order today?")

menu = ["Coffee", "Tea", "Smoothie"]
for item in menu:
    print("- " + item)

order = input("Please select an item from the menu: ")
print("Great choice, " + customer_name + "! Your " + order + " will be ready in a few moments.")

price = 0
if order == "Coffee":
    price = 3.50
elif order == "Tea":
    price = 2.50
elif order == "Smoothie":
    price = 4.00
print("The price of your " + order + " is $" + str(price) + ".")

quantity = int(input("How many would you like to order? "))
total_cost = price * quantity
print("The total cost of your order is $" + str(total_cost) + ".")
