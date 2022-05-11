from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

servent = CoffeeMaker() 
menu = Menu()
# menu_item = MenuItem()
money_machine= MoneyMachine()

machine_on = True
while  machine_on :
    options = menu.get_items()
    prompt=input(f"What would you like ? {options} ").lower()
    if prompt == 'off':
        machine_on=False
    elif prompt == 'report':
        servent.report()
        money_machine.report()
    else:
        drink=menu.find_drink(prompt)
        if servent.is_resource_sufficient(drink) == True:
            print(f"The price of {prompt} is ₹{drink.cost}")
            if money_machine.make_payment(drink.cost) == True:
              servent.make_coffee(drink)