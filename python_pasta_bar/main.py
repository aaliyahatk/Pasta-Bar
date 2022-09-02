def get_integer(m):
    user_input = int(input(m))
    return user_input

#printmenu
def print_menu(l):
    for x in l:
        print(x[0].upper())
        output = "{} ${}".format(x[1], x[2])
        print(output)

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
    this_order = [Pasta_lists[index][0], quantity, Pasta_lists[index][2]]
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
        menu = ["P: Print Menu",  "A: Add to order", "Q: Quit"]
        for x in menu:
            print(x)
        choice = input("What would you like to do?")
        if choice == "P":
            print_menu(Pasta_lists)
        elif choice == "A":
            add_to_order(Pasta_lists, Customer_order)
        elif choice == "Q":
            run = False
        else:
            print("Unrecognised entry")


if __name__ == '__main__':
    main()
