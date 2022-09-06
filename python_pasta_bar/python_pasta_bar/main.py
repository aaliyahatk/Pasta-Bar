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
    # calculating subtotal of order
    subtotal_price = Pasta_lists[index][2] * quantity
    # output of reviewing order
    this_order = "{} {} at ${} each with a sub-total cost of ${}".format(quantity, Pasta_lists[index][0],
                                                                     Pasta_lists[index][2], subtotal_price)
    Customer_order.append(this_order)
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
        menu = ["P: Print Menu", "A: Add to order", "R: Review order","Q: Quit"]
        for x in menu:
            print(x)
        choice = input("What would you like to do?")
        # print menu when P is selected
        if choice == "P":
            print_menu(Pasta_lists)
        # add to order when A is selcted
        elif choice == "A":
            add_to_order(Pasta_lists, Customer_order)
        # review customer order option
        elif choice == "R":
            review_pasta(Customer_order)
        # option to quit
        elif choice == "Q":
            run = False
        # no valid entry will not work
        else:
            print("Unrecognised entry")


if __name__ == '__main__':
    main()
