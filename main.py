MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def insert_coin():
    print("Please insert coins")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.05
    return total


def check_resource(resource, drink):
    if MENU[drink]["ingredients"]["water"] > resource["water"]:
        print("sorry, not enough water on the machine")
    elif MENU[drink]["ingredients"]["coffee"] > resource["coffee"]:
        print("sorry, not enough coffee on the machine")
    elif MENU[drink]["ingredients"]["milk"] > resource["milk"]:
        print("sorry, not enough milk on the machine")
    else:
        total = insert_coin()
        if MENU[drink]["cost"] > total:
            print("Sorry that's not enough money. Money refunded!")
        else:
            change = total - MENU[drink]["cost"]
            change = round(change, 2)
            print(f"Here's your change ${change}")
            print(f"here's your {drink} ☕, enjoy!!")
            resource["water"] -= MENU[drink]["ingredients"]["water"]
            resource["coffee"] -= MENU[drink]["ingredients"]["coffee"]
            resource["milk"] -= MENU[drink]["ingredients"]["milk"]
            resource["money"] += MENU[drink]["cost"]


def machine_report(resource):
    print(f"Water : {resource['water']}ml")
    print(f"Milk : {resource['milk']}ml")
    print(f"Coffee : {resource['coffee']}g")
    print(f"Money : ${resource['money']}")


machine = "on"
while machine == "on":
    answer = input("What would you like?(espresso/latte/cappuccino):")
    if answer == "off":
        machine = "off"
        break
    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        check_resource(resources, answer)
    elif answer == "report":

        machine_report(resources)
