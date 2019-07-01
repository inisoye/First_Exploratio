# Assignment Q1:  Create a functioning shopping cart

#* First, a dictionary of the items for sale is created.
print('All prices provided are in NGN')
oranges = {'Name': 'Madagascan Oranges', 'Price': 50, 'Quantity Available': 15}
pineapples = {'Name': 'Beninese Pineapples', 'Price': 400, 'Quantity Available': 4}
cucumbers = {'Name': 'Ogbomoso Cucumbers', 'Price': 90, 'Quantity Available': 29}
plums = {'Name': 'Arabian Plums', 'Price':250, 'Quantity Available': 37}
satsumas = {'Name': 'Egyptian Satsumas', 'Price': 70, 'Quantity Available': 13}
apples = {'Name': 'Scottish Apples', 'Price': 100, 'Quantity Available': 64}

list_of_fruit_dicts = [oranges, pineapples, cucumbers, plums, satsumas, apples]
print('The items available for sale are provided below: \n')
for fruits in list_of_fruit_dicts:
    item_name = fruits['Name']
    item_price = fruits['Price'] #*! For some reason, these variables need to be defined. Cant be concatenated directly. WHY?
    item_quantity = fruits['Quantity Available']
    print(f'Item {(list_of_fruit_dicts.index(fruits))+1}: {item_name}, Price: {item_price}, Quantity Available: {item_quantity}')

# while True:
#     item_selector = int(input('Enter the number of the item you will like to add to your cart: '))
#     quantity_selector = int(input('How many of these items will you like to buy? '))
#     while item_selector <= len(list_of_fruit_dicts):
#         item_name = fruits['Name']
#         if item_selector == 1:
#             order_price = quantity_selector*oranges['Price']
#             oranges['Quantity Available'] -= 1
#             print(item_name)
#             continue_request = input('Will you like to order another item? (If yes, enter 1. If no, enter 0.)')
#             if continue_request:
#                 continue
#             else:
#                 print("order summary")  #todo insert order summary here
#         elif item_selector == 2:
#             order_price = quantity_selector*pineapples['Price']
#             pineapples['Quantity Available'] -= 1
#             break
#         elif item_selector == 3:
#             order_price = quantity_selector*cucumbers['Price']
#             cucumbers['Quantity Available'] -= 1
#             break
#         elif item_selector == 4:
#             order_price = quantity_selector*plums['Price']
#             plums['Quantity Available'] -= 1
#             break
#         elif item_selector == 5:
#             order_price = quantity_selector*satsumas['Price']
#             satsumas['Quantity Available'] -= 1
#             break
#         elif item_selector == 6:
#             order_price = quantity_selector*apples['Price']
#             apples['Quantity Available'] -= 1
#             break
#         else:
#             print('Only the items listed above can be ordered, please pick a correct item')

