#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

starting_names = []
with open("Input/Names/invited_names.txt") as names: 
    starting_names = [name.strip() for name in names]  # list of lines


template = open("Input/Letters/starting_letter.txt").read()

for name in starting_names:
    with open(f"Output/ReadyToSend/{name}.txt", mode = "w") as letter:
        x = template.replace("[name]", name)
        letter.write(x)