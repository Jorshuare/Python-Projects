import time


# Define your functions
def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")


def get_drink_type():
    res = input('\nWhat type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>: ').lower()
    if res == "a":
        return "brewed coffee"
    elif res == "b":
        return "mocha"
    elif res == "c":
        return order_latte()
    else:
        print_message()
        return get_drink_type()


def order_latte():
    res = input('\nAnd what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>: ').lower()
    if res == "a":
        return "latte"
    elif res == "b":
        return "non-fat latte"
    elif res == 'c':
        return "soy latte"
    else:
        print_message()
        return order_latte()


def get_size():
    print('Please type either a, b or c for each of the question')
    time.sleep(2)
    res = input('\nWhat size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>: ').lower()
    if res == "a":
        return "small"
    elif res == "b":
        return "medium"
    elif res == "c":
        return 'large'
    else:
        print_message()
        return get_size()


def coffee_bot():
    print("Welcome to the cafe!")
    time.sleep(1)

    size = get_size()
    drink_type = get_drink_type()
    print('\nAlright, that\'s a {} {}!'.format(size, drink_type))

    name = input('Can I get your name please? \n> ')
    time.sleep(2)
    print("Thanks, {}! Your drink '{} {}' will be ready shortly.".format(name, size, drink_type))


# Call coffee_bot()!
coffee_bot()
