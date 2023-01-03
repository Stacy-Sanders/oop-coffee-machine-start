from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def get_coffee():
    # TODO: 1. Ask what they want to drink, repeat until user enters "off"
    drink_choice = input(f"What would you like? ({menu.get_items()}):  ").lower()
    # TODO: 2. Turn off the prompt when "off" is input
    if drink_choice == "off":
        return "off"
    # TODO: 3. Print report when prompted
    elif drink_choice == "report":
        return f"{coffee_maker.report()}\n{money_machine.report()}"
    # TODO: 4. Check if drink is available
    else:
        drink_info = menu.find_drink(drink_choice)
        if drink_info:
            availability = coffee_maker.is_resource_sufficient(drink_info)
            if availability:
                # TODO: 5. Accept payment, check amount, return change if necessary
                sale = money_machine.make_payment(drink_info.cost)
                if sale:
                    # TODO: 6. Present drink
                    return coffee_maker.make_coffee(drink_info)
                else:
                    return sale

            else:
                return availability

        else:
            return drink_info


is_on = True

while is_on:
    response = get_coffee()
    if response == "off":
        is_on = False
    else:
        response
