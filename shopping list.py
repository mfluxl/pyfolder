#Extra Mile:
#OS to clear the terminal.
#TIME to delay terminal prints.

import os
import time

shopping_list = []
shopping_list_price = []
keep_adding = ""
userchoice = ""
cost = ""


def welcome():
    
    print("Choose an option from the menu to start.")
    print("*" * 10)
    print(f"1.ADD items\n2.DISPLAY the contents of the shopping cart \n3.REMOVE an item \n4.Compute the TOTAL \n5.Quit\n")

   
def add_items():
    j = input("Add an item to the list: ")
    k = input("Price: ")
    shopping_list.append(j)
    shopping_list_price.append(k)
    keep_adding = j


def display_items():
    for i in range(len(shopping_list)):
        product = shopping_list[i]
        cost = shopping_list_price[i]
        print(f"{i}. {product.title()} ${cost}")
        
    
#def remove_item():


#def find_total():


print("\n\nWelcome to you shopping list program!")

while userchoice != "4" or userchoice != "quit":
    welcome()
    userchoice = input("Choose from the menu: ").lower()

    if userchoice == "1" or userchoice == "add":
        j = input("Add an item to the cart: ")
        k = input("Price: ")
        shopping_list.append(j)
        shopping_list_price.append(k)
        keep_adding = j
                
    elif userchoice == "2" or userchoice == "display":
        os.system('cls')
        for i in range(len(shopping_list)):
            product = shopping_list[i]
            cost = shopping_list_price[i]
            print(f"{i}. {product.title()} ${cost}")
        time.sleep(2)
        
    elif userchoice == "3" or userchoice == "remove":
        #remove_item()
        removed_product = input("What item would you like to remove from the cart? ").strip().lower()
        price_delete = shopping_list.index(removed_product)
        shopping_list.remove(removed_product)
        shopping_list_price.pop(price_delete)     

        os.system("cls")
        print(f"Item {removed_product} removed.\n")
        print("Updated list:")
        display_items()
        time.sleep(2)

    elif userchoice == "4" or userchoice == "total":
        #find_total()
        total = 0
        #print(list(map(int, shopping_list_price)))
        total = sum(list(map(int, shopping_list_price)))
        print(f"The total price of the items in the shopping cart is ${total}")

    else:
        print("Invalid command!")
        

