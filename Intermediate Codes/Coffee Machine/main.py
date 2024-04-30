from database import MENU
from database import resources

machine_resources = resources
amount = 0.0
is_on = True
entries = []
passkey = "password"


def refill_machine():
    measure = ""
    print("Here are the following stats for this machine:")
    for key in machine_resources:
        measure = "g" if key == "coffee" else "ml"
        print(f"{key.title()}: {machine_resources[key]}{measure}")

    print(f"Cash: ${amount}")
    target_ingredient = input("What ingredient do you want to refill?")
    if MENU.get(target_ingredient) is None:
        print("Invalid Ingredient")
        return
    refill_amount = input(f"what's the amount in {measure}")
    if not refill_amount.isnumeric():
        print("Invalid refill amount")
        return

    machine_resources[target_ingredient] += refill_amount


def authenticate():
    if input("Input password for access: ") == passkey:
        return True
    else:
        print("Incorrect Password")
        return False


def check_storage(data, order):
    item = MENU.get(order)
    ingredients = item["ingredients"]
    in_storage = True
    for ingredient in ingredients:
        if data[ingredient] < ingredients[ingredient]:
            in_storage = False

    return in_storage


def update_resources(data, order):
    item = MENU.get(order)
    ingredients = item["ingredients"]
    for ingredient in ingredients:
        data[ingredient] -= ingredients[ingredient]


def process_payment(order):
    global entries
    quarters = input("How many quarters: ")
    dimes = input("How many dimes: ")
    nickels = input("How many nickels: ")
    pennies = input("How many pennies: ")

    if not quarters.isnumeric() or not dimes.isnumeric() or not nickels.isnumeric() or not pennies.isnumeric():
        return False, 0, "Invalid Inputs"

    total_value = (int(quarters) * 0.25) + (int(dimes) * 0.10) + (int(nickels) * 0.05) + (int(pennies) * 0.01)

    cost = MENU.get(order)["cost"]

    if total_value >= cost:
        change = total_value - cost
        entries.append(f"Payment for '{order.title()}' with ${change} change")
        return True, change, "Payment Successful"
    else:
        return False, 0, "Insufficient Amount"


def generate_report(data, cash, logs):
    print("Here are the following stats for this machine:")
    for key in data:
        measure = "g" if key == "coffee" else "ml"
        print(f"{key.title()}: {data[key]}{measure}")

    print(f"Cash: ${cash}")

    if len(entries) < 1:
        return

    show_log = True if input("Would you like to see the entry log? Y/N").upper() == "Y" else False
    if show_log:
        print("Here are the payments recorded in the machine...")
        for log in logs:
            print(log)


def machine_process():
    global is_on, amount, machine_resources
    order = input("What would you like to order/command? ").lower()
    if MENU.get(order) is None:
        if order == "off":
            is_on = False
        elif order == "menu":
            print(f"Here's our menu: (espresso,latte,cappuccino)")
        elif order == "report":
            if authenticate():
                generate_report(machine_resources, amount, entries)
        elif order == "refill":
            if authenticate():
                refill_machine()
        else:
            print("Invalid Order/Command")
    else:
        if check_storage(machine_resources, order):
            success, change, message = process_payment(order)
            print("Processing Payment...")
            if success:
                update_resources(machine_resources, order)
                amount += MENU.get(order)["cost"]
                print(message)
                print(f"Here's your change of ${change} after payment process")
                print(f"Here's your {order}, Enjoy!")
            else:
                print(f"Error Processing Payment \nERR_MSG: {message}")
        else:
            print("Insufficient resources")


while is_on:
    machine_process()
