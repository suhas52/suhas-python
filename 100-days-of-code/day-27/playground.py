def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,5,7))

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)