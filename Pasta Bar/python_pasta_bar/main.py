# Set global variable for total
total = 0


# validation
def get_integer(m):
    user_input = input(m)
    while user_input.isnumeric() is False:
        user_input = input("Please insert a number: ")
    return int(user_input)


# printmenu
def print_menu(l):
    for x in l:
        print(x[0].upper())
        output = "{} ${}".format(x[1], x[2])
        print(output)
    return None


# review pasta
def review_pasta(customer_order):
    print(customer_order)
    global total
    print("Current total is $", total)
    return None


# adding pasta to orders
def add_to_order(pasta_lists, customer_order):
    """
    :param pasta_lists: list
    :param customer_order: list
    :return: None
    """

    c = 0
    for x in pasta_lists:
        output = "{:<5}{:<10} -- {:>4}".format(c, x[0], x[2])
        print(output)
        c += 1
    # get valid options
    values = int(len(pasta_lists)) - 1
    # Test print
    # print (values)
    # adding pasta to order
    index = get_integer("What pasta would you like to add to your order?")
    if (values) >= index >= 0:
        message = "How many {} would you like".format(pasta_lists[index][0])
        quantity = get_integer(message)
        # calculating subtotal of added items
        subtotal_price = pasta_lists[index][2] * quantity
        # calculate total using global variable
        global total
        total = total + subtotal_price
        print("Current total is $", total)
        # output of reviewing order
        this_order = "{} {} at ${} each with a sub-total cost of ${}".format(quantity, pasta_lists[index][0],
                                                                             pasta_lists[index][2], subtotal_price)
        customer_order.append(this_order)
    else:
        print("Please enter a valid option")
    return None


# delete pasta from orders
def delete_from_order(customer_order):
    """
    :param customer_order: list
    :return: None
    """

    # Testing
    # print(customer_order)

    c = 0
    for x in customer_order:
        output = "{:<5}{:<5}".format(c, x)
        print(output)
        c += 1

    # get valid options
    values = int(len(customer_order)) - 1
    # Test print
    # print (values)

    # delete pasta from order
    index = get_integer("What pasta would you like delete from your order?")
    if index <= (values) and index >= 0:
        # Get subtotal and remove from total
        subtotal_price = int((customer_order[index].split("$")[-1]))
        # Test - print
        # print(subtotal_price)
        global total
        total = total - subtotal_price
        # Remove from order
        customer_order.remove(customer_order[index])
        print("Current total is $", total)
    else:
        print("Please enter a valid option")
    return None


# complete order
def complete_order(customer_order):
    # Use global variable
    global total
    # Print order
    print("Your order is", customer_order)
    name = input("What is the name for the order?")
    delivery = input(
        "Will you pickup or would you like the pasta delivered for $3? Please enter "
        "D for delivery or any other character for pickup.")
    if delivery == "D":
        total = total + 3
        print("The total cost is $", total)
        number = input("What is your mobile number?")
        addr = input("What is the address for the order?")
        print("Thanks for the order", name, number, "We will deliver to", addr, "as soon as possible!")
    else:
        total = total
        print("The total cost is $", total)
        print("Thanks for the order", name, "See you soon for pickup!")
    # Clear order and total now it is complete
    customer_order.clear()
    total = 0
    return None


def main():
    # pasta list with descriptions and prices
    pasta_lists = (
        ["Fusilli Pesto", "Short, spiral pasta. Kale and cashew pesto and cream sauce, olives, parmesan", 19],
        ["Conchilglie alla Bolognese", "Small, shell pasta. Northern italian beef and pork sauce, parmesan", 22],
        ["Spaghetti Pomodoro", "Long, thin pasta. Classic tomato and basil sauce, parmesan", 16],
        ["Pappardelle Ricci D'Angelo",
         "Short, frizzy pasta. Slow cooked lamb ragu, rosemary, olives, sweet garlic, parmesan", 26],
        ["Fettuccine Carbonara", "Long, flat pasta. Creamy egg and pepper sauce, bacon, parmesan", 20])
    customer_order = []
    run = True
    while run is True:
        # menu options
        menu = ["P: Print Menu", "A: Add to order", "D: Delete from order", "R: Review order", "C: Complete Order",
                "Q: Quit"]
        for x in menu:
            print(x)
        choice = input("What would you like to do?")
        # print menu when P is selected
        if choice == "P":
            print_menu(pasta_lists)
        # add to order when A is selected
        elif choice == "A":
            add_to_order(pasta_lists, customer_order)
        # delete from order when D is selected
        elif choice == "D":
            delete_from_order(customer_order)
        # review customer order option
        elif choice == "R":
            review_pasta(customer_order)
        # Complete Order
        elif choice == "C":
            complete_order(customer_order)
        # option to quit
        elif choice == "Q":
            run = False
        # no valid entry will not work
        else:
            print("Unrecognised entry")


if __name__ == '__main__':
    main()
