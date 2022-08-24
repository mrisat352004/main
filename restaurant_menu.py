import time
import sys
def typewrite(message):
    for i in message:
        sys.stdout.write(i)     # This entire code allows the string to be printed slowly, which makes it more userfriendly.
        sys.stdout.flush()
        time.sleep(0.03)    

typewrite("Hey welcome to Felix's burgers!\n")      # Ask the user for their name.
typewrite("What is your name?: ")                   # Then capitalize the input and delete empty spaces.
def hey(to):
    typewrite(f"\nHey {str(to)}, what can we get you?\nHere is our menu for today.") 
name = input()
name = name.strip().title()
hey(name)

# Present the menu to the user.
time.sleep(2)
item_list_burger = ["\nCheeseburger [1] ", "\nDouble Stack Burger [2] ", "\nFelix's Special Burger [3]"]
item_list_chicken = ["\nChicken Sandwich [10] ", "\nSpicy Chicken [20] ", "\nFelix's Special Chicken Sandwich [30]"]

for item in item_list_burger:
    typewrite(item)
for item in item_list_chicken:
    typewrite(item)

#This is unused code                            
"""{    
            {typewrite(f"\n{item_list_burger}, \n{item_list_chicken}")  
                {typewrite(f"\n\nCheeseburger [1]\nDouble Stack Burger [2]\nFelix's Special Burger [3]\n")
                    typewrite(f"\nChicken Sandwich [10]\nSpicy Chicken [20]\nFelix's Special Chicken Sandwich [30]\n")
                }
            }    
        }    """

# Ask the user to enter the menu number of the item they want.
# Based on the number, present the cost of the item and ask user to pay.
item = int(input("\nChoose your item: "))   # User inputs item number
"""while True:
    try:
        item = int(input("\nChoose your item: "))
    except ValueError:
        print("Please enter an item number")"""

def change_due(item_price):                                     # If paid more than the price, the customer will be returned their change.      
    change = item - item_price                                  # If paid less, they will be asked to pay the remaining amount.
    return change
if item == 1: # Cheeseburger 1       
    typewrite(f"Your Cheeseburger is being prepared \nIt is $4.55\n")
    item_price = 4.55
    item = float(input(f"Pay ${item_price} : "))
    if item == 4.55:
        typewrite("Payment successful: Enjoy your meal!")
    elif item > 4.55:
        change_due(item_price)
        typewrite("Payment successful: Here is your change $", change_due, " Enjoy your meal!")
    elif item < 4.55:
        need = item_price - item
        typewrite(f"You are ${need:.2f} short.")
        pay_again = float(input("Please pay the rest: "))
        payment = need + pay_again
        if payment == 4.55:
            typewrite("Thank you: Enjoy your meal!")
        elif payment > 4.55:
            change = pay_again - need
            typewrite(f"Thank you: Here is your change ${change:.2f}, Enjoy your meal!")
    else:
        typewrite("Payment declined: Not enough cash.")

if item == 2: #Double stack 2
    typewrite(f"Your Double Stack Burger is being prepared \nIt is 6.85\n")
    item_price = 6.85
    item = float(input(f"Pay ${item_price} : "))
    if item == 6.85:
        typewrite("Payment successful: Enjoy your meal!")
    elif item > 6.85:
        change = item - item_price
        typewrite(f"Payment successful: Here is your change ${change:.2f}, Enjoy your meal!")
    elif item < 6.85:
        need = item_price - item
        typewrite(f"You are ${need:.2f} short.")
        pay_again = float(input("Please pay the rest: "))
        payment = need + pay_again
        if payment == 6.85:
            typewrite("Thank you: Enjoy your meal!")
        elif payment > 4.55:
            change = pay_again - need
            typewrite(f"Thank you: Here is your change ${change:.2f}, Enjoy your meal!")
    else:
        typewrite("Payment declined: Not enough cash.")

if item == 3: #Special Burger 3
    typewrite(f"Your Felix's Special Burger \nIt is 5.80\n")
    item_price = 5.80
    item = float(input(f"Pay ${item_price} : "))
    if item == 5.80:
        typewrite("Payment successful: Enjoy your meal!")
    elif item > 5.80:
        change = item - item_price
        typewrite(f"Payment Successful: Here is your change ${change:.2f}, Enjoy your meal!")
    elif item < 5.80:
        need = item_price - item
        typewrite(f"You are ${need:.2f} short.")
        pay_again = float(input("Please pay the rest: "))
        payment = need + pay_again
        if payment == 5.80:
            typewrite("Thank you: Enjoy your meal!")
        elif payment > 5.80:
            change = pay_again - need
            typewrite(f"Thank you: Here is your change ${change:.2f}, Enjoy your meal!")
    else:
        typewrite("Payment declined: Not enough cash.")

if item == 10: #Chicken Sandwich 10
    typewrite(f"Your Chicken Sandwich is being prepared \nIt is 4.55\n")
    item_price = 4.55
    item = float(input(f"Pay ${item_price} : "))
    if item == 4.55:
        typewrite("Payment successful: Enjoy your meal!")
    elif item > 4.55:
        change = item - item_price
        typewrite(f"Payment Successful: Here is your change ${change:.2f}, Enjoy your meal!")
    elif item < 4.55:
        need = item_price - item
        typewrite(f"You are ${need:.2f} short.")
        pay_again = float(input("Please pay the rest: "))
        payment = need + pay_again
        if payment == 4.55:
            typewrite("Thank you: Enjoy your meal!")
        elif payment > 4.55:
            change = pay_again - need
            typewrite(f"Thank you: Here is your change ${change:.2f}, Enjoy your meal!")
    else:
        typewrite("Payment declined: Not enough cash.")

if item == 20: #Spicy Chicken [20] 
    typewrite(f"Your Spicy Chicken Sandwich is being prepared \nIt is 4.55\n")
    item_price = 4.55
    item = float(input(f"Pay ${item_price} : "))
    if item == 4.55:
        typewrite("Payment Successful: Enjoy your meal!")
    elif item > 4.55:
        change = item - item_price
        typewrite(f"Payment Successful: Here is your change ${change:.2f}, Enjoy your meal!")
    elif item < 4.55:
        need = item_price - item
        typewrite(f"You are ${need:.2f} short.")
        pay_again = float(input("Please pay the rest: "))
        payment = need + pay_again
        if payment == 4.55:
            typewrite("Thank you: Enjoy your meal!")
        elif payment > 4.55:
            change = pay_again - need
            typewrite(f"Thank you: Here is your change ${change:.2f}, Enjoy your meal!")
    else:
        typewrite("Payment declined: Not enough cash.")


#Felix's Special Chicken Sandwich [30]

if item == 30: #Felix's Special Chicken Sandwich [30]
    typewrite(f"Your Felix's Special Chicken Sandwich is being prepared \nIt is 6.55\n")
    item_price = 6.55
    item = float(input(f"Pay ${item_price} : "))
    if item == 6.55:
        typewrite("Payment Successful: Enjoy your meal!")
    elif item > 6.55:
        change = item - item_price
        typewrite(f"Payment Successful: Here is your change ${change:.2f}, Enjoy your meal!")
    elif item < 6.55:
        need = item_price - item
        typewrite(f"You are ${need:.2f} short.")
        pay_again = float(input("Please pay the rest: "))
        payment = need + pay_again
        if payment == 6.55:
            typewrite("Thank you: Enjoy your meal!")
        elif payment > 6.55:
            change = pay_again - need
            typewrite(f"Thank you: Here is your change ${change:.2f}, Enjoy your meal!")
    else:
        typewrite("Payment declined: Not enough cash.")
