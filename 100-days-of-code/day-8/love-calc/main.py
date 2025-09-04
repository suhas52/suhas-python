def get_names():
    names = []
    for i in range(1,3):
        name = input(f"Please enter name {i}")
        name = name.capitalize()
        names.append(name)
    return names



def true_count(name):
    true_count = 0
    for i in name.upper():
        if i == "T" or i == "R" or i == "U" or i == "E":
            true_count += 1
    return true_count

def love_count(name):
    love_count = 0
    for i in name.upper():
        if i == "L" or i == "O" or i == "V" or i == "E":
            love_count += 1
    return love_count


name1, name2 = get_names()

love_score = str(true_count(name1 + name2)) + str(love_count(name1 + name2))
 
print(love_score)
