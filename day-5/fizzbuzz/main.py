for x in range(1,101):
    out = ""
    if x % 3 == 0:
        out += "Fizz"
    if x % 5 == 0:
        out += "Buzz"
    print (out or x)
