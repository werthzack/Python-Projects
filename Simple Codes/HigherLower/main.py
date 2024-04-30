from game_data import data
import random as rand
import os


def get_random_account():
    random_index = rand.randint(0, len(data) - 1)
    return data[random_index]


prev_account = None
loss = False
score = 0

print("Welcome To Higher-Lower Challenge")

while loss is False:
    os.system('cls' if os.name == "nt" else 'clear')
    print(f"Score: {score}")
    compared_account = ""
    if prev_account is None:
        prev_account = get_random_account()
        compared_account = get_random_account()
    else:
        compared_account = get_random_account()

    size_A = prev_account["follower_count"]
    size_B = compared_account["follower_count"]

    print(f"First Star: {prev_account["name"]}\n")  #You can add '{size_A} to show the size and debug
    print(f"Compared To: {compared_account["name"]}\n")  #You can add '{size_A} to show the size and debug
    decision = input(f"Is {compared_account['name']} Higher [A] or Lower [B]: ").upper()

    if decision != "A" and decision != "B":
        print("Invalid Answer")
        continue

    answer = ""
    if size_B >= size_A:
        answer = "A"
    elif size_A > size_B:
        answer = "B"

    if decision == answer:
        score += 1
        prev_account = compared_account
        compared_account = None
    else:
        print("Wrong Answer! GAME OVER!!")
        loss = True

print(f"Your score is {score}")
