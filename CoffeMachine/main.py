MENU = {"espresso":     {"ingredients": {"water": 50, "coffee": 18}, 
                                "cost": 1.5},
        
        "latte":        {"ingredients": {"water": 200, "milk": 150, "coffee": 24},
                                "cost": 2.5},
    
        "cappuccino":   {"ingredients": {"water": 250, "milk": 100, "coffee": 24},
                                "cost": 3.0},
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {  # VALORES >> MOEDAS
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25,
}





def total_coins(values_coins):
    """Valor total das moedas inseridas"""
    # QUANTIDADE >> MOEDAS
    quarters = int(input('Please insert coins.\nhow many quartes?: '))
    dimes = int(input('how many dimes?: '))
    nickels = int(input('how many nickels?: '))
    pennies = int(input('how many pennies?: '))
    
    quarters *= values_coins['quarter']
    dimes *= values_coins['dime']
    nickels *= values_coins['nickel']
    pennies *= values_coins['penny']

    total = (quarters+dimes+nickels+pennies)
    return total


def stock(products, order):
    for name, amount in products.items():
        water = name == 'water'
        milk = name == 'milk'
        coffee = name == 'coffee'

        if espresso:
            if water:
                products[name] = amount - ingredients['water']
            elif coffee:
                products[name] = amount - ingredients['coffee']
        elif latte or cappuccino:
            if water:
                products[name] = amount - ingredients['water']
            elif milk:
                products[name] = amount - ingredients['milk']
            elif coffee:
                products[name] = amount - ingredients['coffee']

        if amount <= 0:
            return name
    
    return products


coffee_machine = True
bank = 0
while coffee_machine:
    order = input('What would you like? (espresso/latte/cappuccino): ')

    espresso = order == 'espresso'
    latte = order == 'latte'
    cappuccino = order == 'cappuccino'
    report = order == 'report'
    if espresso:
        customer_request = MENU["espresso"]
        ingredients = customer_request['ingredients']
        espresso_resources = stock(resources, order)
        if espresso_resources == 'water' or espresso_resources == 'milk' or espresso_resources == 'coffee':
            print(f'Sorry there is not enough {espresso_resources}.')
            continue
        else:
            bank += customer_request['cost']
            purchase_total = total_coins(coins)
            change = purchase_total - customer_request['cost']
            if change >= 0:
                print(f'Here is ${change:.2f} in change.\nHere is your {order}☕. Enjoy!')
                continue
            elif change < 0:
                print("Sorry that's not enough money. Moneyrefunded")
                continue
    elif latte:
        customer_request = MENU["latte"]
        ingredients = customer_request['ingredients']
        latte_resources = stock(resources, order)
        if latte_resources == 'water' or latte_resources == 'milk' or latte_resources == 'coffee':
            print(f'Sorry there is not enough {latte_resources}.')
            continue
        else:
            bank += customer_request['cost']
            purchase_total = total_coins(coins)
            change = purchase_total - customer_request['cost']
            if change >= 0:
                print(f'Here is ${change:.2f} in change.\nHere is your {order}☕. Enjoy!')
                continue
            elif change < 0:
                print("Sorry that's not enough money. Moneyrefunded")
                continue
    elif cappuccino:
        customer_request = MENU["cappuccino"]
        ingredients = customer_request['ingredients']
        cappuccino_resources = stock(resources, order)
        if cappuccino_resources == 'water' or cappuccino_resources == 'milk' or cappuccino_resources == 'coffee':
            print(f'Sorry there is not enough {cappuccino_resources}.')
            continue
        else:
            bank += customer_request['cost']
            purchase_total = total_coins(coins)
            change = purchase_total - customer_request['cost']
            if change >= 0:
                print(f'Here is ${change:.2f} in change.\nHere is your {order}☕. Enjoy!')
                continue
            elif change < 0:
                print("Sorry that's not enough money. Moneyrefunded")
            continue
    elif report:
        for name, amount in resources.items():
            if name == 'water' or name == 'milk':
                print(f'{name.capitalize()}: {amount}ml')
            else:
                print(f'{name.capitalize()}: {amount}g')
        print(f'Money: ${bank}') 
        continue
    else:
        coffee_machine = False
    