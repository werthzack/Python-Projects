with open("./invite_list.txt") as invite_file:
    invite_list = invite_file.read().split("\n")

with open("./template_letter.txt") as template_file:
    template_data = template_file.read()
    for person in invite_list:
        with open(f"./Ready/{person}'s_Letter.txt","w") as new_letter:
            new_letter.write(template_data.replace("[name]", person))
