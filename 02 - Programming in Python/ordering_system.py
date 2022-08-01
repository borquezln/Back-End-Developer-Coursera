menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

# Calculates the subtotal of an order
def calculate_subtotal(order):
    print('Calculating bill subtotal...')
    subtotal = 0
    for item in order:
        subtotal += item["price"]
    return subtotal

# Calculates the tax of an order
def calculate_tax(subtotal):
    print('Calculating tax from subtotal...')
    tax = subtotal * 0.15
    return round(tax, 2)

# Summarizes the order
def summarize_order(order):
    print_order(order)
    
    subtotal = round(calculate_subtotal(order), 2)
    print("Subtotal for the order is: " + str(subtotal))
    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))
    total = round(subtotal + tax, 2)

    names = []
    names = [item["name"] for item in order]
    
    return names, total

# Prints out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# Displays the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# Creates an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

def main():
    order = take_order()
    items, total = summarize_order(order)
    print("The total bill for your order: ", items, " is $", total, sep="")

if __name__ == "__main__":
    main()
