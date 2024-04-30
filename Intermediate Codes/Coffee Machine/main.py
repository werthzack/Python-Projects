from database import MENU
from database import resources
from os import system

is_on = True


def generate_report():
    pass


def machine_process():
    global is_on
    machine_resources = resources
    order = input("What would you like to order/command? ").lower()
    if MENU.get(order) is None:
        if order == "off":
            is_on = False
        elif order == "menu":
            print(f"Here's our menu: (espresso,latte,cappuccino)")
        elif order == "report":
            generate_report()
        else:
            print("Invalid Order/Command")


while is_on:
    machine_process()
