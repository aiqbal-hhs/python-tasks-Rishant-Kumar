# imports functions that will be used in the program
from collections import namedtuple
import time

# Empty lists to store the orders of user
order_list = []
topping = []

# empty variable for total cost
order_cost = 0

# empty dictionary for Contact information for delivery
user_info = {}

# Dictionary Pizza to price, key = pizza, value = price
pizza_to_price = {
    "Classic Cheese": 8.50,
    "Classic Veggie": 8.50,
    "Pepperoni": 8.50,
    "Margherita": 8.50,
    "Spicy Paneer": 8.50,
    "Tandoori Chicken": 13.50,
    "Peri Peri Chicken": 13.50,
    "BBQ Chicken": 13.50,
    "Garlic Prawn": 13.50,
    "Americano": 8.50,
    "Supreme": 8.50,
    "Spicy Lamb": 13.50,
}

# Index of pizza to price, key= index (number), value = price...
# ...(associated with that number)
index_to_price = {
    "1": 8.50,
    "2": 8.50,
    "3": 8.50,
    "4": 8.50,
    "5": 8.50,
    "6": 8.50,
    "7": 8.50,
    "8": 13.50,
    "9": 13.50,
    "10": 13.50,
    "11": 13.50,
    "12": 13.50,
}

# Index to pizza # Index of pizza to price, key= index (number), 
# value = pizza name
index_to_pizza = {
    "1": "\n- Classic Cheese",
    "2": "\n- Classic Veggie",
    "3": "\n- Pepperoni",
    "4": "\n- Margherita",
    "5": "\n- Spicy Paneer",
    "6": "\n- Americano",
    "7": "\n- Supreme",
    "8": "\n- BBQ Chicken",
    "9": "\n- Garlic Prawn",
    "10": "\n- Tandoori Chicken",
    "11": "\n- Peri Peri Chicken",
    "12": "\n- Spicy Lamb",
}

# defining namedtuple for pizza menu
menu_entry = namedtuple("menu_entry", ["index", "pizza", "price"])
pizza_options = []

# appends pizza options to named tuple
pizza_options.append(menu_entry(1, "Classic Cheese", "$8.50"))
pizza_options.append(menu_entry(2, "Classic Veggie", "$8.50"))
pizza_options.append(menu_entry(3, "Pepperoni", "$8.50"))
pizza_options.append(menu_entry(4, "Margherita", "$8.50"))
pizza_options.append(menu_entry(5, "Spicy Paneer", "$8.50"))
pizza_options.append(menu_entry(6, "Americano", "$8.50"))
pizza_options.append(menu_entry(7, "Supreme", "$8.50"))
pizza_options.append(menu_entry(8, "BBQ Chicken", "$13.50"))
pizza_options.append(menu_entry(9, "Garlic Prawn", "$13.50"))
pizza_options.append(menu_entry(10, "Tandoori Chicken", "$13.50"))
pizza_options.append(menu_entry(11, "Peri Peri Chicken", "$13.50"))
pizza_options.append(menu_entry(12, "Spicy Lamb", "$13.50"))

# toppings to price list
index_to_topping = {
    "1": " + Extra Cheese",
    "2": " + Extra Onions",
    "3": " + Extra Mushroom",
    "4": " + Extra Pepperoni",
    "5": " + Extra Olives",
    "6": " + Extra Chicken",
}

# defining namedtuple for Toppings Menu
topping_entry = namedtuple("topping_entry", ["index", "topping", "price"])
topping_options = []

# appends topping options to named tuple
topping_options.append(topping_entry(1, "Extra Cheese", "$0.50"))
topping_options.append(topping_entry(2, "Extra Onion", "$0.50"))
topping_options.append(topping_entry(3, "Extra Mushroom", "$0.50"))
topping_options.append(topping_entry(4, "Extra Pepperoni", "$0.50"))
topping_options.append(topping_entry(5, "Extra Olives", "$0.50"))
topping_options.append(topping_entry(6, "Extra Chicken", "$0.50"))


# prints and formats the pizza menu
def pizza_menu():
    print("\n\033[4;34m\033[1;94mOur selection of pizzas:\033[0m")
    for entry in pizza_options:
        index = str(getattr(entry, "index")).ljust(5)
        pizza = getattr(entry, "pizza").ljust(25)
        price = getattr(entry, "price").ljust(7)
        time.sleep(0.1)
        print(
            "\033[1;92m{}\033[0m\033[1;34m{}\033[0m\033[1;91m{}\033[0m"
            .format(index, pizza, price)
        )


# Prints and formats the topping menu
def topping_menu():
    print("\n\033[4;34m\033[1;94mOur selection of toppings:\033[0m")
    for entry in topping_options:
        index = str(getattr(entry, "index")).ljust(5)
        topping = getattr(entry, "topping").ljust(25)
        price = getattr(entry, "price").ljust(7)
        time.sleep(0.2)
        print(
            "\033[1;92m{}\033[0m\033[1;34m{}\033[0m\033[1;91m{}\033[0m"
            .format(index, topping, price)
        )


# main Menu function prints out the instructions for the user so they can use a
# mode option for the Henderson Pizza Palace service.
def main_menu():
    """Prints out the instructions for the user so they can use an action 
    option to use the Henderson Pizza Palace service."""
    print("\n\033[1;97mType: \n")
    time.sleep(0.5)
    print("'1' to view our pizzas and toppings\n")
    time.sleep(0.5)
    print("'2' to order pizza\n")
    time.sleep(0.5)
    print("'3' to cancel/finish ordering\033[0m\n")
    time.sleep(0.5)


# service Menu function prints out the instructions for the user so they
# can use a service option for the Henderson Pizza Palace service.
def servicing_menu(order_cost):
    """Prints out the instructions for the user so they can use a 
    service option for the Henderson Pizza Palace service."""
    print("\n\033[1;97mHow would you like to be receiving your order?\n")
    time.sleep(0.5)
    print("Type:\n")
    time.sleep(0.5)
    print("'1' Delivery ($3 Delivery charge)\n")
    time.sleep(0.5)
    print("'2' Pick-up\n")
    time.sleep(0.5)
    print("'3' Go back to main menu\033[0m")

    global service_option
    service_repeat = True
    while service_repeat:
        service_option = input(
            "\033[1;92m\nInput number here: \033[0m"
        ).strip()
        # Asks the user to input address and phone number
        # Will ask if contact information is correct
        # Will remove contact information and repeat if user inputs "no"
        contact_repeat = True
        # if user selects 1
        if service_option == "1":
            print("\n\033[0;93mService Option: Delivery\033[0m\n")
            time.sleep(1)
            # adds $3 to user order cost as delivery has $3 charge
            order_cost += 3
            print(
                "\033[0;33mLets start gathering your details first..."
                "\033[0m\n"
            )
            time.sleep(1)
            while contact_repeat:
                # non integer error prevention
                try:
                    phone_number = int(
                        input(
                            "\033[1;92mPlease enter your phone number: \033[0m"
                        ).strip()
                    )
                except ValueError:
                    # tells user to enter an appropriate integer and goes back
                    # to phone number input
                    print(
                        "\n\033[1;91m\033[40mPlease input integers only!"
                        "\033[0m\n"
                    )
                    continue

                # adds user phone number to user_info dictionary
                user_info["Phone number"] = phone_number
                print(
                        "\033[0;93mAdded customer's Phone Number..."
                        "\033[0m"
                    )
                time.sleep(1)

                # ask user for address
                address = input(
                    "\033[1;92m"
                    "\nPlease enter your delivery address: \033[0m"
                ).strip()
                # checks if the user has entered a name
                if len(address) > 0:
                    # adds users address to dictionary
                    user_info["Address"] = address.title()
                    print(
                        "\033[0;93mAdded customer's Address..."
                        "\033[0m"
                    )
                    time.sleep(1)
                # if there is no name
                else:
                    print(
                        "\n\033[1;91m\033[40m"
                        "You have not entered an appropriate address! "
                        "Please re-enter it for contacting purposes."
                        "\033[0m\n"
                    )
                    print(
                        "\033[0;93mBacktracking customer's information..."
                        "\033[0m\n"
                    )
                    time.sleep(1)
                    continue

                # ask user for their name
                name = input(
                    "\n\033[1;92mPlease enter your name: \033[0m"
                ).strip()
                # checks if they had entered a name
                if len(name) > 0:
                    # adds users name to dictionary
                    user_info["Name"] = name.title()
                    print(
                        "\033[0;93mAdded customer's Name..."
                        "\033[0m"
                    )
                    time.sleep(1)

                    # if the user has entered no name
                else:
                    print(
                        "\n\033[1;91m\033[40m"
                        "You have entered no name! "
                        "Please re-enter it for contacting purposes."
                        "\033[0m\n"
                    )
                    print(
                        "\033[0;93mBacktracking customer's information..."
                        "\033[0m\n"
                    )
                    time.sleep(1)
                    continue

                print(
                    "\n\033[1;97mYour Contact Information:"
                    "\033[0m\033[1;96m"
                )
                    # prints user info dictionary
                for key, value in user_info.items():
                    print(key, ":", value)

                while True:
                    print(
                        "\033[0m\n\033[1;92m"
                        "Is the contact information shown above correct?"
                        "\033[0m"
                    )
                    # ask to enter yes or no for their contact info
                    correct_info = (
                        input("\033[1;92mAnswer ('Yes' or 'No'): \033[0m")
                        .strip()
                        .lower()
                    )
                    # if no, then they will be sent back to the top of loop
                    if correct_info == "no" or correct_info == "n":
                        print(
                            "\n\033[1;91m"
                            "Please resubmit your contact information"
                            "\033[0m\n"
                        )
                        time.sleep(0.1)
                        print(
                            "\033[0;93m"
                            "Backtracking customer's information..."
                            "\033[0m\n"
                        )
                        time.sleep(1)
                        contact_repeat = True
                        break

                    # when the user enters 'yes'
                    elif correct_info == "yes" or correct_info == "y":
                        # exit loops
                        contact_repeat = False
                        break

                    # if user does not say either 'yes' or 'no'
                    else:
                        print(
                            "\033[1;91m\033[40m"
                            "\nPlease enter a valid response "
                            "('Yes' or 'No')!\033[0m"
                        )
                        continue
        # if user selects 2
        elif service_option == "2":
            print("\n\033[0;93mService Option: Pick-up\033[0m")
            time.sleep(1)
            print("\n\033[0;33mLets start gathering your details first...")
            while contact_repeat:
                name = input(
                    "\n\033[1;92m"
                    "Please enter your name: \033[0m"
                ).strip()
                # checks if the user has entered name
                if len(name) > 0:
                    # adds users name to dictionary
                    user_info["Name"] = name.title()

                else:
                    print(
                        "\n\033[0m\033[1;91m\033[40m"
                        "You have entered no name! "
                        "Please enter one for contating purposes.\033[0m"
                    )
                    print(
                        "\n\033[0;93m"
                        "Backtracking customer's information..."
                        "\033[0m"
                    )
                    time.sleep(1)
                    continue

                # prints users information
                print("\033[1;96m")
                for key, value in user_info.items():
                    print(key, ":", value)
                # asks if the entered details are correct
                while True:
                    print(
                        "\033[0m\n\033[1;92m"
                        "Is the contact information shown above correct?"
                        "\033[0m"
                    )
                    correct_info = (
                        input("\033[1;92mAnswer ('Yes' or 'No'):  \033[0m")
                        .strip()
                        .lower()
                    )
                    # if 'no', then it will go back
                    # to where they start to enter the details
                    if correct_info == "no" or correct_info == "n":
                        print(
                            "\033[1;91mPlease resubmit your name for "
                            "contacting purposes!\n\033[0m"
                        )
                        time.sleep(0.1)
                        print(
                            "\033[0;93m"
                            "Backtracking customer's information..."
                            "\033[0m\n"
                        )
                        time.sleep(1)
                        contact_repeat = True
                        break
                    # if 'yes', then they will continue to order section
                    elif correct_info == "yes" or correct_info == "y":
                        # exit loops
                        contact_repeat = False
                        break
                    # if they enter anything else other than
                    # 'yes or no', loops back to the top
                    else:
                        print(
                            "\n\033[1;91m\033[40m"
                            "Please enter a valid response ('Yes' or 'No')!"
                            "\033[0m"
                        )
                        continue

        # heads back to main menu by exiting loop when user enters '3'
        elif service_option == "3":
            print("\033[0;93mHeading back to Main menu...\033[0m")
            time.sleep(1)
            break

        # if they enter anything else other than '1, 2 or 3',
        # loops back to the top
        else:
            print(
                "\n\033[1;91m\033[40m"
                "Please input a valid number (either '1', '2' or '3')"
                "\033[0m"
            )
            continue

        service_repeat = False

    time.sleep(1)


# Function that takes in the users orders
def order(order_cost, topping):
    order_loop = 0
    while order_loop < 5:
        # prints the instuctions and pizza menu
        pizza_menu()
        print(
            "\n\033[0;95m"
            "Order using the number next to the name of the pizza."
        )
        time.sleep(0.5)
        print("To finish ordering, type 'end'.")
        time.sleep(0.5)
        print("To cancel ordering, type 'cancel'.")
        time.sleep(0.5)
        print("Maximum 5 pizzas per customer.\033[0m")
        time.sleep(0.5)
        new_order = (
            input(
                "\n\033[1;92m"
                "Input Pizza number here: \033[0m"
            ).strip().lower()
        )
        # when user enters 'end' or ordering loops 5 times, prints users order,
        # cost, user info and also confirms order
        if new_order == "end":
            break

        # if number in index_to_pizza dictionary,
        # then pizza name is appended to order_list
        elif new_order in index_to_pizza:
            order_loop += 1
            order_list.append(index_to_pizza.get(new_order))
            # if the number entered by user is associate with a pizza,
            # then price will be added and will move on to toppings
            if new_order in index_to_price:
                # adds cost of pizza to order_cost
                order_cost += index_to_price.get(new_order)
                # prints what user has ordered
                print(
                    "\033[1;34m"
                    "Ordered {}."
                    "\033[0m"
                    .format(index_to_pizza.get(new_order))
                )
                topping_menu()
                time.sleep(1)
                # prints instructions
                print(
                    "\033[0;95m"
                    "\nAdd toppings using the number next to the "
                    "name of the topping."
                    "\nMaximum 3 toppings allowed per pizza."
                )
                time.sleep(1)
                print("To finish adding toppings, type 'end'.\033[0m")
                topping_loop = 0
                # topping loop (max 3 times)
                while topping_loop < 3:
                    topping = (
                        input("\n\033[1;92mInput topping number here: \033[0m")
                        .strip()
                        .lower()
                    )
                    # if topping in dictionary, adds it to order_list
                    if topping in index_to_topping:
                        topping_loop += 1
                        order_list.append(index_to_topping.get(topping))
                        order_cost += 0.5
                        print(
                            "\033[1;34mAdded '{}' to pizza.\033[0m".format(
                                index_to_topping.get(topping)
                            )
                        )
                        time.sleep(1)
                        # prints current cost
                        print(
                            "\n\033[1;91m"
                            "Current total cost of order is: ${:.2f}\033[0m"
                            .format(order_cost)
                        )
                        time.sleep(1)
                        continue
                    # if user enters 'end',
                    # breaks out of loop and prints current cost (exits)
                    elif topping == "end":
                        print(
                            "\n\033[1;91m"
                            "Current total cost of order is: ${:.2f}\033[0m"
                            .format(order_cost)
                        )
                        break
                    # if user enters something else,
                    # warns them and goes back to the top of loop
                    else:
                        print(
                            "\n\033[1;91m\033[40m"
                            "That is not one of the topping options!"
                            "\033[0m"
                        )
                        continue
                # if topping looped 3 times
                # then this message is printed to the user and prints cost
                if topping_loop == 3:
                    print(
                        "\n\033[0;101m\033[1;90m"
                        "You have reached the maximum number of toppings you "
                        "can order per pizza (3)!"
                        "\033[0m"
                    )
                    time.sleep(1)
                    print(
                        "\n\033[1;91m"
                        "Current total cost of order is: ${:.2f}"
                        "\033[0m"
                        .format(order_cost)
                    )
                    continue

                else:
                    pass

                time.sleep(2)

        # when user enters 'cancel', they will be sent back to the main menu
        # and order_list will be cleared
        elif new_order == "cancel":
            # resets by clearing order_list and tells the user that
            order_list.clear()
            order_cost = 0
            topping_loop = 0
            print(
                "\033[0;93mOrder cleared!\033[0m"
                "\n\033[0;93mHeading back to Main menu...\033[0m"
            )
            time.sleep(1)
            break
        # if the user does not enter the appropriate number
        # then prints this message and goes back to the top of loop
        else:
            print(
                "\n\033[1;91m\033[40m"
                "Sorry, that is not one of the pizza options!"
                "\033[0m"
            )
            time.sleep(2)
            continue
    # when the main ordering loop loops 5 times
    # then this message is printed to warn the user
    if order_loop == 5:
        print(
            "\n\033[0;101m\033[1;90mYou have reached the "
            "maximum number of pizzas you can order per customer (5)!\033[0m"
        )
        time.sleep(2)

    else:
        pass
    # confirms order loop
    while len(order_list) > 0:
        # shows user their information
        print("\n\033[1;97mContact Information:\033[0m\n\033[1;96m")
        for key, value in user_info.items():
            print(key, ":", value)
        # prints their order
        print("\n\033[1;97mYou have ordered:\033[0m")
        view_order()
        print(
            "\n\033[1;91mTotal cost of order: ${:.2f}"
            "\033[0m"
            .format(order_cost)
        )
        time.sleep(1)
        print(
            "\n\033[0;95m"
            "If your order is correct, type 'Yes'to continue"
            "\nIf your order is incorect, type 'No' to reorder"
            "\033[0m"
        )

        correct_order = (
            input(
                "\033[1;92m"
                "\nIs your order correct? (Please input 'Yes' or 'No'): "
                "\033[0m"
            )
            .strip()
            .lower()
        )
        # when the user confirms order, then prints appreciation message
        if correct_order == "yes" or correct_order == "y":
            print(
                "\033[1;37m\033[4;37m"
                "\nYour order will be ready soon! "
                "Thanks for ordering at Henderson Pizza Palace!\n"
                "\033[0m"
            )
            time.sleep(2)
            break

        # if the order is incorrect, the order list will be cleared
        elif correct_order == "no" or correct_order == "n":
            print("\n\033[0;33mLets backtrack your order...")
            time.sleep(1)
            order_list.clear()
            order_cost = 0
            print("Previous order list cleared...\033[0m")
            time.sleep(1)
            order(order_cost, topping)
            break
        # if user enters anything other than 'yes' or 'no'
        # the prints warning message
        else:
            print("\n\033[1;91m\033[40mPlease enter 'Yes' or 'No'\033[0m")
            time.sleep(1)
            continue

    return order_cost


# Function that shows current orders in the order_list
def view_order():
    if len(order_list) > 0:
        for order in order_list:
            print("\033[1;96m{}\033[0m".format(order, topping))
            time.sleep(0.25)

    else:
        print("\n\033[1;91m\033[40mYou have no orders!\033[0m")


# Running main program loop (calling functions etc)
print("\n\033[1;37m\033[4;37mHenderson Pizza Palace\033[0m\n")
time.sleep(0.5)
# user initial instructions
print(
    "\033[1;97m\n"
    "Hello, Welcome to Henderson Pizza Palace text-based ordering system."
    "\nBelow is our Main menu, "
    "please enter a number associated with your required service."
    "\nMaximum of 5 pizzas per customer and 3 toppings per pizza"
)
print(
    "\nEnter the required service and your details before ordering pizzas."
    "\033[0m"
    )
time.sleep(3.5)

repeat = True
while repeat:
    # Ask user for number input
    # Prints main menu
    main_menu()
    time.sleep(0.75)
    main_menu_option = input("\033[1;92mInput number Here: \033[0m").strip()

    # Checking input and calls appropriate function -
    # this one calls the food menus
    if main_menu_option == "1":
        print("\n\033[0;33mView pizza and topping menus...\033[0m")
        time.sleep(1)
        pizza_menu()
        time.sleep(1)
        topping_menu()
        time.sleep(1)

    # this one calls the servicing and order functions
    elif main_menu_option == "2":
        # if the user enters 2 after ordering,
        # then list is cleared and they continue
        # otherwise they continue
        if len(order_list) > 0:
            print("\n\033[1;91m\033[40mYou have already ordered!\033[0m")
            print(
                "\n\033[0;95m"
                "Do you want to continue? "
                "\nIf 'Yes', then the previous order will be cleared.\n"
                "If 'No', then you will be outed."
                "\033[0m"
            )
            user_continue = input(
                "\n\033[1;92m"
                "'Yes' or 'No': "
                "\033[0m"
                ).strip().lower()

            # if yes, clears order_list and continues to servicing and ordering
            if user_continue == "yes" or user_continue == "y":
                print("\033[0;33mPrevious order list cleared...\033[0m")
                order_list.clear()

            # program ends
            elif user_continue == "no" or user_continue == "n":
                print(
                    "\n\033[1;37m\033[4;37m"
                    "Thanks for purchasing from Henderson Pizza Palace!"
                    "\nHope to see you again {}!"
                    "\033[0m"
                    .format(user_info["Name"])
                )
                time.sleep(1)
                break

            # if user enters anything else other than 'yes' or 'no'
            else:
                print(
                    "\033[1;91m\033[40mPlease enter 'Yes' or 'No'!"
                    "\033[0m\n"
                    .format(main_menu_option)
                )
        else:
            pass

        print("\n\033[0;33mChoose a service option...")
        time.sleep(1)
        # calls service menu
        servicing_menu(order_cost)
        if service_option == "3":
            continue
        print("\n\033[0;33mLets start ordering...")
        time.sleep(1)
        # calls order menu
        order(order_cost, topping)

    # program ends
    elif main_menu_option == "3":
        # if there is an order, then prints a thank you message with users name
        if len(order_list) > 0:
            print(
                "\033[1;37m\033[4;37m"
                "Thanks for purchasing from Henderson Pizza Palace!"
                "\nHope to see you again {}!\033[0m".format(user_info["Name"])
            )
            # clears order list
            order_list.clear()
            break
        # if there is no order, tells user thanks for visiting
        else:
            print("\n\033[1;37m\033[4;37mThanks for visiting!\033[0m\n")
            break

    # if user does not enter the correct set of numbers
    else:
        print(
            "\033[1;91m\033[40m"
            "'{}' wasn't an option"
            "\033[0m\n"
            .format(main_menu_option)
        )
