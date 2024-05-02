from machine_OOP import CoffeeMachine
from database import MENU

new_machine = CoffeeMachine()


def machine_process():
    order = input("What would you like to order/command? ").lower()
    if MENU.get(order) is None:
        if order == "off":
            new_machine.is_on = False
        elif order == "menu":
            print(f"Here's our menu: (espresso,latte,cappuccino)")
        elif order == "report":
            if new_machine.authenticate():
                new_machine.generate_report()
        elif order == "refill":
            if new_machine.authenticate():
                new_machine.refill_machine()
        else:
            print("Invalid Order/Command")
    else:
        if new_machine.check_storage(order):
            success, change, message = new_machine.process_payment(order)
            print("Processing Payment...")
            if success:
                new_machine.update_resources(order)
                new_machine.amount += MENU.get(order)["cost"]
                print(message)
                print(f"Here's your change of ${change} after payment process")
                print(f"Here's your {order}, Enjoy!")
            else:
                print(f"Error Processing Payment \nERR_MSG: {message}")
        else:
            print("Insufficient resources")


while new_machine.is_on:
    machine_process()
