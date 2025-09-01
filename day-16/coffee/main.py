import coffee_maker
from menu import Menu
import money_machine
import sys

menu = Menu()
coffee_machine = coffee_maker.CoffeeMaker()
money_machine = money_machine.MoneyMachine()

while True:
	choice = input(f"What would you like? ({menu.get_items()}) ")
	if choice == "off":
		sys.exit()
	if choice == "report":
		print(coffee_machine.report())
		print(money_machine.report())
	else:
		user_drink = menu.find_drink(choice)
		if coffee_machine.is_resource_sufficient(user_drink):
			if money_machine.make_payment(user_drink.cost):
				coffee_machine.make_coffee(user_drink)
			else:
				print("Sorry that's not enough money. Money refunded.")
		else:
			print('Sorry there is not enough water.')
	
