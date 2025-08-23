weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: "))

bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi} and you're underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your bmi is {bmi} and you're of normal weight.")
elif bmi > 25 and bmi < 150:
    print(f"Your bmi is {bmi} and you're overweight.")
else:
    print("Please enter valid values.")
