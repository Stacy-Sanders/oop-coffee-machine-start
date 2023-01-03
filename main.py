from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True


while is_on:
    # TODO: 1. Ask what they want to drink, repeat until user enters "off"
    choice = input(f"What would you like? ({menu.get_items()}):  ").lower()
    # TODO: 2. Turn off the prompt when "off" is input
    if choice == "off":
        is_on = False
    # TODO: 3. Print report when prompted
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    # TODO: 4. Check if drink is available
    else:
        drink = menu.find_drink(choice)
        if drink:
            # TODO: 5. if resources are sufficient and correct payment, make drink
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
