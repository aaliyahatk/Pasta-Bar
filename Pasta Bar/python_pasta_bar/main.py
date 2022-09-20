# Set global variable for total
total = 0


def get_integer(m):
    user_input = int(input(m))
    return user_input


# printmenu
def print_menu(l):
    for x in l:
        print(x[0].upper())
        output = "{} ${}".format(x[1], x[2])
        print(output)
    return None


# review pasta
def review_pasta(Customer_order):
    print(Customer_order)
    return None


# adding pasta to orders
def add_to_order(Pasta_lists, Customer_order):
    """
    :param Pasta_lists: list
    :param Customer_order: list
    :return: None
    """

    c = 0
    for x in Pasta_lists:
        output = "{:<5}{:<10} -- {:>4}".format(c, x[0], x[2])
        print(output)
        c += 1
    # adding pasta to order
    index = get_integer("What pasta would you like to add to your order?")
    message = "How many {} would you like".format(Pasta_lists[index][0])
    quantity = get_integer(message)
    # calculating subtotal of added items
    subtotal_price = Pasta_lists[index][2] * quantity
    # calculate total using global variable
    global total
    total = total + subtotal_price
    print("Current total is $", total)
    # output of reviewing order
    this_order = "{} {} at ${} each with a sub-total cost of ${}".format(quantity, Pasta_lists[index][0],
                                                                         Pasta_lists[index][2], subtotal_price)
    Customer_order.append(this_order)
    return None


# delete pasta from orders
def delete_from_order(Customer_order):
    """
    :param Customer_order: list
    :return: None
    """

    # Testing
    # print(Customer_order)

    c = 0
    for x in Customer_order:
        output = "{:<5}{:<5}".format(c, x)
        print(output)
        c += 1

    # delete pasta from order
    index = get_integer("What pasta would you like delete from your order?")
    Customer_order.remove(Customer_order[index])
    # Need to delete from total. How?
    return None


# complete order
def complete_order(Customer_order):
    # Use global variable
    global total
    # Print order
    print("Your order is", Customer_order)
    name = input("What is the name for the order?")
    delivery = input(
        "Will you pickup or would you like the pasta delivered for $3? Please enter D for delivery or any other character for pickup.")
    if delivery == "D":
        total = total + 3
        print("The total cost is $", total)
        addr = input("What is the address for the order?")
        print("Thanks for the order", name, "We will deliver to", addr, "as soon as possible!")
    else:
        total = total
        print("The total cost is $", total)
        print("Thanks for the order", name, "See you soon for pickup!")
    # Clear order and total now it is complete
    Customer_order.clear()
    total = 0
    return None


def main():
    # pasta list with descriptions and prices
    Pasta_lists = (
        ["Fusilli Pesto", "Short, spiral pasta. Kale and cashew pesto and cream sauce, olives, parmesan", 19],
        ["Conchilglie alla Bolognese", "Small, shell pasta. Northern italian beef and pork sauce, parmesan", 22],
        ["Spaghetti Pomodoro", "Long, thin pasta. Classic tomato and basil sauce, parmesan", 16],
        ["Pappardelle Ricci D'Angelo",
         "Short, frizzy pasta. Slow cooked lamb ragu, rosemary, olives, sweet garlic, parmesan", 26],
        ["Fettuccine Carbonara", "Long, flat pasta. Creamy egg and pepper sauce, bacon, parmesan", 20])
    Customer_order = []
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
            print_menu(Pasta_lists)
        # add to order when A is selcted
        elif choice == "A":
            add_to_order(Pasta_lists, Customer_order)
        # delete from order when D is selected
        elif choice == "D":
            delete_from_order(Customer_order)
        # review customer order option
        elif choice == "R":
            review_pasta(Customer_order)
        # Complete Order
        elif choice == "C":
            complete_order(Customer_order)
        # option to quit
        elif choice == "Q":
            run = False
        # no valid entry will not work
        else:
            print("Unrecognised entry")


if __name__ == '__main__':
    main()