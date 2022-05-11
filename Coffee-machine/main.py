from numpy import True_


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 100,
}
money=0

def check_rescource(ingredients):
    for item in ingredients:
        if ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}.😐")
            return 0
    return 1

def coins():
    print("Please insert coins")
    total=int(input("How many 20 rupees note/coin  "))*20
    total+=int(input("How many 10 rupees note/coin "))*10
    total+=int(input("How many 5 rupees notes/coin "))*5
    total+=int(input("How many 2 rupees coin  "))*2
    return total


def transaction_succesfull(payment,cost):
    if payment>=cost:
        if payment>cost:
            print(f"Here is your rs {payment-cost} in change")
        global money
        money += drink["cost"]
        return True
    elif payment<cost:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-= order_ingredients[item]
    
    print(f"Here is your {drink_name}. Enjoy!☕") 
    
machine_on = True
while  machine_on :
    prompt=input("What would you like ? ").lower()
    if prompt == 'off':
        machine_on=False
    elif prompt == 'report':
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}gm")
        print(f"Money : Rs {money}")
    else:
        drink=MENU[prompt]
        if check_rescource(drink["ingredients"]) == 1:
            print(f"The price of {prompt} is {drink['cost']}")
            payment=coins()
            if transaction_succesfull(payment,drink["cost"])==True:
                make_coffee(prompt,drink["ingredients"])




