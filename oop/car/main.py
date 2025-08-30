class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def ran_mileage(self):
        return f"The {self.color} car has {self.mileage} miles."

red = Car("red", 30000)
blue = Car("blue", 20000)

print(red.ran_mileage())
print(blue.ran_mileage())
