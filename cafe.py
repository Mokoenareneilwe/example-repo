menu = ["Coffee", "Sandwich", "Latte", "Mocha", "cake"]

# dictionary with menu items as keys and stock quantities as values
stock = {"Coffee": 10, "Sandwich": 5, "Latte": 8, "Mocha": 6, "cake": 5}

# dictionary with menu items as keys and prices as values
price = {"Coffee": 3.50, "Sandwich": 5.00, "Latte": 4.00, "Mocha": 4.50, "cake": 5.00}

for item in menu:
    total_stock = stock[item] * price[item]
    print ( menu [menu.index(item)] + ": R" + str(total_stock))
