def add(x, y):
    print(x + y)

def substract(x, y):
    print(x - y)

def multiply(x, y):
    print(x * y)

def divide(x, y):
    print(x / y)

def choose(x, y):
    while True:
        choice = input("Please choose one of the following +, - , * or /: ")
        match choice:
            case "+":
                add(x, y)
                break
            case "-":
                substract(x, y)
                break
            case "*":
                multiply(x, y)
                break
            case "/":
                divide(x, y)
                break
        print("Please enter a valid operator.")
                
x = int(input("input a value for x: "))
y = int(input("Input a value for y: "))

choose(x, y)
