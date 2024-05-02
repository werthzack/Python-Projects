from database import resources as prod
from database import prices
from database import MENU


class CoffeeMachine:
    def __init__(self, password="password"):
        self.is_on = True
        self.resources = prod
        self.entries = []
        self.passkey = password
        self.amount = 0.0

    def refill_machine(self):
        measure = ""
        print("Here are the following stats for this machine:")
        for key in self.resources:
            measure = "g" if key == "coffee" else "ml"
            print(f"{key.title()}: {self.resources[key]}{measure}")

        target_ingredient = input("What ingredient do you want to refill? ").lower()
        if self.resources.get(target_ingredient) is None:
            print("Invalid Ingredient")
            return
        print(f"To refill {target_ingredient}, it's ${prices[target_ingredient]} per {measure}")
        print(f"Cash: ${self.amount}")
        refill_amount = input(f"what's the amount in {measure} ")
        if not refill_amount.isnumeric():
            print("Invalid refill amount")
            return

        total_amount = int(refill_amount) * prices[target_ingredient]
        confirmation = True if (input(f"Here's the total amount: ${total_amount}, confirm purchase? Y/N ").upper()
                                == "Y") else False
        if confirmation:
            if self.amount < total_amount:
                print("Not enough Cash")
                self.refill_machine()
            self.resources[target_ingredient] += int(refill_amount)
            self.amount -= total_amount
            print(f"Ingredient '{target_ingredient.title()}' has been refilled")
            self.entries.append(f"Purchased ${total_amount} worth of ingredient '{target_ingredient.title()}' "
                                f"equivalent to {refill_amount}{measure}")
            command = input("Do you want make another refill?(refill)")
            if command == "refill":
                self.refill_machine()

    def authenticate(self):
        if input("Input password for access: ") == self.passkey:
            return True
        else:
            print("Incorrect Password")
            return False

    def check_storage(self, order):
        item = MENU.get(order)
        ingredients = item["ingredients"]
        in_storage = True
        for ingredient in ingredients:
            if self.resources[ingredient] < ingredients[ingredient]:
                in_storage = False

        return in_storage

    def update_resources(self, order):
        item = MENU.get(order)
        ingredients = item["ingredients"]
        for ingredient in ingredients:
            self.resources[ingredient] -= ingredients[ingredient]

    def process_payment(self, order):
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
            self.entries.append(f"Payment for '{order.title()}' with ${change} change")
            return True, change, "Payment Successful"
        else:
            return False, 0, "Insufficient Amount"

    def generate_report(self):
        print("Here are the following stats for this machine:")
        for key in self.resources:
            measure = "g" if key == "coffee" else "ml"
            print(f"{key.title()}: {self.resources[key]}{measure}")

        print(f"Cash: ${self.amount}")

        if len(self.entries) < 1:
            return

        show_log = True if input("Would you like to see the entry log? Y/N ").upper() == "Y" else False
        if show_log:
            print("Here are the payments recorded in the machine...")
            for log in self.entries:
                print(log)
