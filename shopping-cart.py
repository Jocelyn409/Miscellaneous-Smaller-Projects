colors = {"apple":"red", "banana":"yellow", "orange":"orange", "pear":"green",
          "kiwi":"brown", "peach":"red", "mango":"yellow", "avacado":"brown"}
shelf = {"apple":0.4, "banana":0.1, "orange":1, "pear":0.45,
         "kiwi":0.8, "peach":0.6, "mango":1.4, "avacado":1.1}
cart = {}

while True:
    print("\nItem colors: " + str(colors) +
          "\nPriced items on shelf: " + str(shelf) +
          "\nPriced items in cart: " + str(cart))

    selection1 = input("\nType CART to move an item to your cart, "
                      "\nSHELF to move an item to the shelf, "
                      "\nand END to stop the program: ").upper()
    if "CART".startswith(selection1):
        selection2 = input("\nType PRICE to move item(s) based on their price, "
                           "\nNAME to move items based on their name, "
                           "\nand COLOR to move items based on their color: ").upper()
        if "PRICE".startswith(selection2):
            selection3 = input("\nChoose to take all items MORE or LESS expensive "
                               "\n(inclusive) than the price selected, "
                               "or EQUAL to it: ").upper()
            try:
                price = float(input("\nChoose a price: "))
            except ValueError:
                print("\nEnter a valid price.")
            if "LESS".startswith(selection3):
                for x, y in shelf.copy().items(): # Searching copy of shelf...
                    if y <= price:
                        switch = shelf.pop(x)  # Get value
                        cart[x] = switch  # Add item to cart
            elif "MORE".startswith(selection3):
                for x, y in shelf.copy().items():
                    if y >= price:
                        switch = shelf.pop(x)
                        cart[x] = switch
            elif "EQUAL".startswith(selection3):
                for x, y in shelf.copy().items():
                    if y == price:
                        switch = shelf.pop(x)
                        cart[x] = switch
            else:
                print("\nEnter a valid answer.")
        elif "NAME".startswith(selection2):
            item = input("\nSelect an item to be put into your shopping cart: ").lower()
            for x in shelf.copy(): # Searching copy of shelf...
                if x == item:
                    switch = shelf.pop(x) # Get value
                    cart[x] = switch # Add item to cart
        elif "COLOR".startswith(selection2):
            color = input("\nEnter a color: ").lower()
            for x, y in colors.items():
                if y == color and x in shelf: # Fruit must be on shelf, and colors must match
                    switch = shelf.pop(x)
                    cart[x] = switch
        else:
            print("\nEnter a valid answer.")

    elif "SHELF".startswith(selection1):
        selection2 = input("\nType PRICE to move item(s) based on their price, "
                           "\nNAME to move items based on their name, "
                           "\nand COLOR to move items based on their color: ").upper()
        if "PRICE".startswith(selection2):
            selection3 = input("\nChoose to take all items MORE or LESS expensive "
                               "\n(inclusive) than the price selected, "
                               "or EQUAL to it: ").upper()
            try:
                price = float(input("\nChoose a price: "))
            except ValueError:
                print("\nEnter a valid price.")
            if "LESS".startswith(selection3):
                for x, y in cart.copy().items(): # Searching copy of cart...
                    if y <= price:
                        switch = cart.pop(x)  # Get value
                        shelf[x] = switch  # Add item to cart
            elif "MORE".startswith(selection3):
                for x, y in cart.copy().items():
                    if y >= price:
                        switch = cart.pop(x)
                        shelf[x] = switch
            elif "EQUAL".startswith(selection3):
                for x, y in cart.copy().items():
                    if y == price:
                        switch = cart.pop(x)
                        shelf[x] = switch
            else:
                print("\nEnter a valid answer.")
        elif "NAME".startswith(selection2):
            item = input("\nSelect an item to be put back on the shelf: ").lower()
            for x in cart.copy(): # Searching copy of cart...
                if x == item:
                    switch = cart.pop(x) # Get value
                    shelf[x] = switch # Add item to shelf
        elif "COLOR".startswith(selection2):
            color = input("\nEnter a color: ").lower()
            for x, y in colors.items():
                if y == color and x in cart: # Fruit must be in cart, and colors must match
                    switch = cart.pop(x)
                    shelf[x] = switch
        else:
            print("\nEnter a valid answer.")
    elif selection1 == "END":
        break
    else:
        print("\nEnter a valid answer.")
