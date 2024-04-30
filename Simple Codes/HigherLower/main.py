from game_data import data
import random as rand
import os

def get_choice():
    random_index = rand.randint(0,len(data)-1)
    return data[random_index]["name"],random_index

def get_size(index):
    return data[index]["follower_count"]


prev_choice = None
prev_index = 0
loss = False
score = 0
print("Welcome To Higher-Lower Challenge")
while loss == False:
    os.system('cls' if os.name == "nt" else 'clear')
    print(f"Score: {score}")
    new_choice = ""
    if prev_choice == None:
        prev_choice,prev_index = get_choice()
        new_choice,new_index = get_choice()
    else:
        new_choice,new_index = get_choice()

    size_A = get_size(prev_index)
    size_B = get_size(new_index)

    print(f"First Star: {prev_choice}  {size_A}\n")   
    print(f"Compared To: {new_choice}  {size_B}\n")
    decision = input(f"Is {new_choice} Higher [A] or Lower [B]: ").upper()

    if decision != "A" and decision != "B":
        print("Invalid Answer")
        next
    
    if size_B >= size_A:
        answer = "A"
    elif size_A > size_B:
        answer = "B"
    

    if decision == answer:
        score += 1
        prev_choice,prev_index = new_choice,new_index
    else:
        loss = True
    
print(f"Your score is {score}")