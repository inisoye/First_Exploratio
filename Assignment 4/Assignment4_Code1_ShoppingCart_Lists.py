# Assignment Q1:  Create a functioning shopping cart

#* First, a dictionary of the items for sale is created. Only fruits were chosen to be sold.
oranges = {'Name': 'Madagascan Oranges', 'Price': 50, 'Quantity Available': 15}
pineapples = {'Name': 'Beninese Pineapples', 'Price': 400, 'Quantity Available': 4}
cucumbers = {'Name': 'Ogbomoso Cucumbers', 'Price': 90, 'Quantity Available': 29}
plums = {'Name': 'Arabian Plums', 'Price':250, 'Quantity Available': 37}
satsumas = {'Name': 'Egyptian Satsumas', 'Price': 70, 'Quantity Available': 13}
apples = {'Name': 'Scottish Apples', 'Price': 100, 'Quantity Available': 64}

#* A list of all the dictionaries (and their entries) are also created below.
list_of_fruit_dicts = [oranges, pineapples, cucumbers, plums, satsumas, apples]
# list_of_fruit_names = [fruits['Name'] for fruits in list_of_fruit_dicts]
# list_of_fruit_prices = [fruits['Price'] for fruits in list_of_fruit_dicts]
# list_of_fruit_quantities = [fruits['Quantity Available'] for fruits in list_of_fruit_dicts]

#* A for loop is used to create a comprehensible list of items for sale.
print('\nThe items available for sale are provided below')
print('All prices provided are in NGN \n')
for fruits in list_of_fruit_dicts:
    item_name = fruits['Name']
    item_price = fruits['Price'] #*! For some reason, these variables need to be defined. Can't be concatenated directly in print function. WHY?
    item_quantity = fruits['Quantity Available']
    print(f'Item {(list_of_fruit_dicts.index(fruits))+1}: {item_name}, Price: {item_price}, Quantity Available: {item_quantity}')

#* Two variables which allow user to enter their item choices are created.
item_selector = int(input('\nEnter the number of the item you will like to add to your cart: '))
quantity_selector = int(input('\nHow many of this item will you like to buy? '))

#* An empty cart, in which the user will add their choices.
cart = []
while True:
    while item_selector <= len(list_of_fruit_dicts):
        if item_selector == 1:
            #* If statement makes sure the user does not request more items than what is available in stock
            if quantity_selector > oranges['Quantity Available']:
                #? Why does the f'' concatenation not work here?
                print('Only ' + str(oranges['Quantity Available']) + ' orange(s) are available')
                break
            #* Else, the choice is added to the cart and removed from the stock
            else:
                order_price = quantity_selector*oranges['Price']
                oranges['Quantity Available'] -= quantity_selector
                oranges['Price'] = order_price
                oranges['Quantity Ordered'] = quantity_selector
                cart.append(oranges)
                print(f'\nYour current cart: {cart}')
                break
        elif item_selector == 2:
            if quantity_selector > pineapples['Quantity Available']:
                print('Only ' + str(pineapples['Quantity Available']) + ' pineapple(s) are available')
                break
            else:
                order_price = quantity_selector*pineapples['Price']
                pineapples['Quantity Available'] -= quantity_selector
                pineapples['Price'] = order_price
                pineapples['Quantity Ordered'] = quantity_selector
                cart.append(pineapples)
                print(f'\nYour current cart: {cart}')
                break
        elif item_selector == 3:
            if quantity_selector > cucumbers['Quantity Available']:
                print('Only ' + str(cucumbers['Quantity Available']) + ' cucumber(s) are available')
                break
            else:
                order_price = quantity_selector*cucumbers['Price']
                cucumbers['Quantity Available'] -= quantity_selector
                cucumbers['Price'] = order_price
                cucumbers['Quantity Ordered'] = quantity_selector
                cart.append(cucumbers)
                print(f'\nYour current cart: {cart}')
                break
        elif item_selector == 4:
            if quantity_selector > plums['Quantity Available']:
                print('Only ' + str(plums['Quantity Available']) + ' plum(s) are available')
                break
            else:
                order_price = quantity_selector*plums['Price']
                plums['Quantity Available'] -= quantity_selector
                plums['Price'] = order_price
                plums['Quantity Ordered'] = quantity_selector
                cart.append(plums)
                print(f'\nYour current cart: {cart}')
                break
        elif item_selector == 5:
            if quantity_selector > satsumas['Quantity Available']:
                print('Only ' + str(satsumas['Quantity Available']) + ' satsuma(s) are available')
                break
            else:
                order_price = quantity_selector*satsumas['Price']
                satsumas['Quantity Available'] -= quantity_selector
                satsumas['Price'] = order_price
                satsumas['Quantity Ordered'] = quantity_selector
                cart.append(satsumas)
                print(f'\nYour current cart: {cart}')
                break
        elif item_selector == 6:
            if quantity_selector > apples['Quantity Available']:
                print('Only ' + str(apples['Quantity Available']) + ' apple(s) are available')
                break
            else:
                order_price = quantity_selector*apples['Price']
                apples['Quantity Available'] -= quantity_selector
                apples['Price'] = order_price
                apples['Quantity Ordered'] = quantity_selector
                cart.append(apples)
                print(f'\nYour current cart: {cart}')
                break

#* Under same umberella while-loop, the user is asked if they will order more. If yes, user is redirected to previous if-else statements
    continue_request = int(input('\nWill you like to order another item? (If yes, enter any nonzero item. If no, enter 0 or None.) '))
    if continue_request:
        item_selector = int(input('\nEnter the number of the item you will like to add to your cart: '))
        quantity_selector = int(input('\nHow many of this item will you like to buy? '))
        continue #! How can i make this go back to the top of the 'while item_selector' loop, starting the process again.
    else:
    #* If user doesn't want to order more, an option for item removal is created below
        remove_request = int(input('\nWill you like to remove an item from your cart? (If yes, enter any nonzero item. If no, enter 0 or None.) '))
        if remove_request:
            print('\nSelect the item you will like to remove from the list below:\n')
            for fruits in list_of_fruit_dicts:
                item_name = fruits['Name']
                item_price = fruits['Price']
                item_quantity = fruits['Quantity Available']
                print(f'Item {(list_of_fruit_dicts.index(fruits))+1}: {item_name}, Price: {item_price}, Quantity Available: {item_quantity}')
            remove_selector = int(input('\nEnter the number of the item you will like to remove your cart: '))
            # remove_quantity = int(input('How many of this item will you like to remove? ')) #todo Remove quantity ignored temporarily
#*[oranges, pineapples, cucumbers, plums, satsumas, apples]
            if remove_selector == 1:
                cart.remove(oranges)
                #! The todo below is necessary, removed item needs to be added back to original stock
                #todo oranges['Quantity Available'] += remove_quantity
                print(f'\nYour updated cart: {cart}')
                continue
            elif remove_selector == 2:
                cart.remove(pineapples)
                print(f'\nYour updated cart: {cart}')
                continue
            elif remove_selector == 3:
                cart.remove(cucumbers)
                print(cart)
                print(f'\nYour updated cart: {cart}')
                continue
            elif remove_selector == 4:
                cart.remove(plums)
                print(f'\nYour updated cart: {cart}')
                continue
            elif remove_selector == 5:
                cart.remove(satsumas)
                print(f'\nYour updated cart: {cart}')
                continue
            elif remove_selector == 6:
                cart.remove(apples)
                print(f'\nYour updated cart: {cart}')
                continue
            continue #! there appears to be an issue with this break and the other continues!
        else:
            print(f'Order Confirmation: {cart}')
            print('Thank you for your order.')
            break