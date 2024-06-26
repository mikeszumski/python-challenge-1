# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = [] # initialize empty order listl

"""
Contents of the order list and dictionary elements within
[
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  }
]
"""

# Launch the store and present a greeting to the customer
print("\nWelcome to the variety food truck!  Please select a menu: ")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order

    # Create a variable for the menu item number
    menu_item_number = 0
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_selection = input("\nEnter menu number: ")

    # Check if the customer's input is a number
    if menu_selection.isdigit():
        # Check if the customer's input is a valid option 
        menu_selection_int = int(menu_selection)
        if menu_selection_int in menu_items.keys():
            # Save the menu category name to a variable
            menu_selection_name = menu_items[menu_selection_int]
            # Print out the menu category name they selected
            print(f"You selected {menu_selection_name}")

            # Print out the menu options from the menu_selection_name
            print(f"What {menu_selection_name} item would you like to order?")
            i = 1
            menu_items = {}     # reuse menu_items variable for sub menu
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_selection_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_item_selected = input('Enter menu item number: ')

            # 3. Check if the customer typed a number
            if menu_item_selected.isdigit():
                # Convert the menu selection to an integer
                menu_item_sel_int = int(menu_item_selected)

                # 4. Check if the menu selection is in the menu items
                if menu_item_sel_int >= 1 and menu_item_sel_int <= i:
                    # Store the item name as a variable
                    #print('menu item sel int',menu_item_sel_int)
                    item_sel_name = menu_items[menu_item_sel_int]["Item name"]
                    item_sel_unitprice = menu_items[menu_item_sel_int]["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f'How many {item_sel_name}, please (default is 1) ')

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity_int = int(quantity)
                    else:
                        quantity_int = 1

                    # Add the item name, price, and quantity to the order list
                    order_list.append({"Item name": item_sel_name,
                                       "Price": item_sel_unitprice,
                                       "Quantity": quantity_int})

                    # Tell the customer that their input isn't valid
                else: 
                    print("Invaid selection, please try again")

                # Tell the customer they didn't select a menu option
            else:
                print("Invalid menu option. Try again. ")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_selection} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("Please enter a menu number (1-4): ")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        # 5. Check the customer's input
        keep_ordering = keep_ordering.lower()
        
        match keep_ordering:
                # Keep ordering

            case 'y':
                place_order = True  # means we want to order more
                break   # exit the while True loop

                # Exit the keep ordering question loop

            case 'n':
                place_order = False # means we don't want to order more
                break   # exit the while True loop

            case _:  #anything other than Y or N
                print('Please try again. Enter Y or N ')
                # Tell the customer to try again
        


# Print out the customer's order
print("\nThis is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order_list)

# 6. Loop through the items in the customer's order
print(" Item name                | Price | Quantity ")
print("--------------------------|-------|----------")

for order_detail in order_list:
    item_name = order_detail["Item name"]
    price = order_detail["Price"]
    quantity = order_detail["Quantity"]
    num_item_spaces = 24 - len(item_name)
    item_spaces = " " * num_item_spaces
    print(f" {item_name}{item_spaces} | ${price} |     {quantity}")
    

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
#print(order_list)

cost_of_order = sum([o["Price"] * o["Quantity"] for o in order_list])

print(f"\nTotal cost of your order is ${cost_of_order}.\n")

