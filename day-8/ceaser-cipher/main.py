alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_choice():
    choice = "x"
    while choice != "decode" and choice != "encode":
        choice = input("Please type if you want to encode or decode a message: ")
    if choice == "encode":
        return True
    else:
        return False

def get_message():
    return input("Please enter your message: ")

def get_shift():
    return int(input("Type the shift number: "))

def encode(message, shift):
    encoded_message = []
    for _ in message:
        char = chr(ord(_) + shift)
        encoded_message.append(char)
    return encoded_message

def decode(message, shift):
    decoded_message = []
    for _ in message:
        char = chr(ord(_) - shift)
        decoded_message.append(char)
    return decoded_message

def start_over():
    retry = "x"
    while retry != "y" and retry != "n":
        retry = input("Do you want to start the program again? (y/n): ")
    if retry == "y":
        return True
    if retry == "n":
        return False
    
retry = True
while retry == True:
    choice = get_choice()
    message = get_message()
    shift = get_shift()
    if choice:
        print(''.join(encode(message, shift)))
    else:
        print(''.join(decode(message,shift)))
    retry = start_over()