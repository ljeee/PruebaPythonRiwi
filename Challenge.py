#Welcome :D
#Inventory diccionary
Inventory = {
    "popcorn": {"Price": 5.10, "Quantity": 10},
    "coke": {"Price": 20.30, "Quantity": 3},
    "chocoramo": {"Price": 15.40, "Quantity": 10},
    "sparkies": {"Price": 1.00, "Quantity": 30},
    "lolete": {"Price": 0.00, "Quantity": 1},
}
#AddProducts
def AddProducts(Inventory, Product, Price, Quantity):
    #Introduce name of the product
    while True:
        print("------------------------------------------")
        Product = input("Introduce the Product name: ").lower().strip()
        if Product in ["exit", "end", "finish"]:
            print("------------------------------------------")
            print("\033[1;31mExiting...\033[0m")
            return
        elif not Product:
            print("------------------------------------------")
            print("\033[1;31mProduct name cannot be empty\033[0m")
            continue
        elif Product in Inventory:
            print("------------------------------------------")
            print("\033[1;31mThat product already exits\033[0m")
            print("------------------------------------------")
        else:
            print("------------------------------------------")
            print(f"\033[1;32mProduct {Product.title()} added\033[0m")
            break
    #Looking for a Valid Product Price   
    while True:
        Price = input("Introduce the price of the product: ")
        if Price in ["exit", "end", "finish"]:
            print("------------------------------------------")
            print("\033[1;31mExiting...\033[0m")
            return
        elif not Price:
            print("\033[1;31mIntroduce a Price pls\033[0m")
            continue
        elif Price.isalpha():
            print("\033[1;31mPrice must be a number, no letters\033[0m")
        elif Price.replace('.', '', 1).isdigit():
            Price = float(Price)
            if Price <= -1:
                print("\033[1;31mPrice must be greater than 0\033[0m")
            else:
                print(f"\033[1;32mPrice of {Product.title()} added\033[0m")
                break
        else:
            print("\033[1;31mPrice must be a valid number\033[0m")
    #Looking for a Valid Product Quantity    
    while True:
        Quantity = input("Enter the Product quantity: ").strip()
        if Quantity in ["exit", "salir", "end"]:
            print("----------")           
            print("\033[1;31mExiting...\033[0m")
            return
        if not Quantity:
            print("------------------------------------------")
            print("\033[1;31mQuantity cannot be empty\033[0m")
        elif Quantity.isdigit():
            Quantity = int(Quantity)
            if Quantity <= -1:
                print("\033[1;31mQuantity must be greater than 0\033[0m")
            else:
                print(f"\033[1;32mQuantity of {Product.title()} added\033[0m")
                break
        else:
            print("\033[1;31mQuantity must be a valid numbers\033[0m")

    #Saving Data
    Inventory[Product] = ({"Price": Price, "Quantity": Quantity})
    print("------------------------------------------")
    print(f"\033[1;34mProduct {Product.title()} added with Price ${Price:.2f} and quantity: {Quantity}\033[0m")
    return Inventory

#AskProductsDetails
def AskProductsDetails(Product, Inventory):
    print("Enter the name of the Product to search or type 'exit' to return to the menu: ")
    while True:
        Product = input("Enter the name of the Product to search: ").lower().strip()
        if Product in ["exit", "salir", "end"]:
            print("----------")           
            print("\033[1;31mExiting...\033[0m")
            return
        if not Product:
            print("------------------------------------------")
            print("\033[1;31mProduct name cannot be empty\033[0m")
            print("------------------------------------------")
        elif Product in Inventory:
            Details = Inventory[Product]
            print("------------------------------------------")
            print(f"\033[1;34mProduct: {Product.title()} | Price: ${Details['Price']:.2f} | Quantity: {Details['Quantity']}\033[0m")
            break
        else:
            print("------------------------------------------")
            print(f"\033[1;31mThe Product {Product.title()} is not in the inventory. Please try again or exit\033[0m")
            print("------------------------------------------")
            
#Upadte Product Information by option
def UpdateProductInfo():
    FullInventory()
    while True:
        print("------------------------------------------")
        #Looking for product
        LookForProduct = input("Enter the name of the product to update or type 'exit' to return to the menu: ").strip().lower()
        if LookForProduct in ["salir", "exit", "end"]:
            print("----------")           
            print("\033[1;31mExiting...\033[0m")
            return
        if not LookForProduct:
            print("------------------------------------------")
            print("\033[1;31mThe name cannot be empty\033[0m")
        elif LookForProduct in Inventory:
            while True:
                #Chose a option
                WhatYouWantToChange = input("What do you want to change? Price/Quantity: ").strip().lower()
                if WhatYouWantToChange in ["salir", "exit", "end"]:
                    print("----------")           
                    print("\033[1;31mExiting...\033[0m")
                    return  
                elif WhatYouWantToChange in ["price", "precio", "value", "valor"]:
                    while True:
                        ChangePrice = input("What is the new price? ").strip()
                        if not ChangePrice:
                            print("\033[1;31mCan't be none\033[0m")
                        elif ChangePrice.isalpha():
                            print("\033[1;31mNo letters\033[0m")
                        elif ChangePrice.replace('.', '', 1).isdigit():
                            ChangePrice = float(ChangePrice)
                            if ChangePrice <= -1:
                                print("\033[1;31mPrice must be greater than 0\033[0m")
                            else:
                                Inventory[LookForProduct]['Price'] = ChangePrice
                                print("------------------------------------------")
                                print(f"\033[1;34mThe price of {LookForProduct.title()} has been updated to {ChangePrice:.2f}\033[0m")
                                return
                        else:
                            print("\033[1;31mPlease follow instructions a number integer\033[0m")
                elif WhatYouWantToChange in ["quantity", "cantidad", "stock"]:
                    while True:
                        ChangeQuantity = input("What is the new quantity? ").strip()
                        if not ChangeQuantity:
                            print("\033[1;31mCan't be none\033[0m")
                        elif ChangeQuantity.isalpha():
                            print("\033[1;31mNo letters\033[0m")
                        elif ChangeQuantity.isdigit():
                            ChangeQuantity = int(ChangeQuantity)
                            if ChangeQuantity < -1:
                                print("\033[1;31mThe quantity cannot be less than 0, or are you giving it away?\033[0m")
                            else:
                                Inventory[LookForProduct]['Quantity'] = ChangeQuantity
                                print("------------------------------------------")
                                print(f"\033[1;34mThe quantity of {LookForProduct.title()} has been updated to {ChangeQuantity}\033[0m")
                                return
                        else:
                            print("\033[1;31mPlease follow instructions a number integer\033[0m")
                else:
                    print("\033[1;31mPlease follow instructions and enter a option\033[0m")
        else:
            print("------------------------------------------")
            print(f"\033[1;31mThe product {LookForProduct.title()} is not in the inventory\033[0m")
 
#Delete Products :B
def DelProduct(Inventory):
    if Inventory:
        print("------------------------------------------")
        print("\033[1;34m Inventory:\033[0m")
        print("------------------------------------------")
        for Product in Inventory:
            print(f"\33[1;31m-> {Product.title()}\033[0m")
        while True:
            Eliminar = input("Enter the name of the product to delete or type exit to return to the menu: ").strip().lower()
            print("------------------------------------------")
            if Eliminar in ["salir", "exit"]:
                print("\033[1;31mExiting...\033[0m")
                break
            elif Eliminar in Inventory:
                del Inventory[Eliminar]
                print(f"\33[1;31mProduct {Eliminar.title()} removed\33[0m")
                break
            elif not Eliminar:
                print("\033[1;31mThe name cannot be empty\033[0m")
                print("------------------------------------------")
            else:
                print(f"\033[1;31mThe product {Eliminar.title()} is not in the inventory\033[0m")
                print("------------------------------------------")
    else:
        print("------------------------------------------")
        print("\033[1;31mNo products in the inventory\033[0m")
        

# TotalValue first check the inventory then make the total value
def TotalValue(Inventory):
    if not Inventory:
        print("------------------------------------------")
        print("\033[1;31mNo products in the inventory\033[0m")
        return 0.0
    TotalValue = lambda items: sum(details["Price"] * details["Quantity"] for details in items.values())
    value = TotalValue(Inventory)
    print("------------------------------------------")
    print(f"\033[1;34m Total value of the inventory: ${value:.2f}\033[0m")
    return value

#FullInventory displays the hole inventory
#I think this is necesary because you need to know the status of the stock
def FullInventory():
    if not Inventory:
        print("------------------------------------------")
        print("\033[1;31mNo products in the inventory\033[0m")
    else:
        print("------------------------------------------")
        print("\033[1;34mThis is the list of products in the inventory\033[0m")
        print("------------------------------------------")
        for Product, details in Inventory.items():
            print(f"\033[1;32mProduct: {Product.title()} | Price: ${details['Price']:.2f} | Quantity: {details['Quantity']}\033[0m")

#Menu
def Menu():
    while True:
        print("------------------------------------------")
        print("\033[1;32mWeclome to the inventory mangament system\033[0m")
        print("------------------------------------------")
        print("1. Add Products")
        print("2. Search for product")
        print("3. Update product info")
        print("4. Delete product")
        print("5. Total stock value")
        print("6. Show Full Inventory")
        print("7. Exit | End | Finish | Close")
        print("------------------------------------------")
        Option = input("Selec a option to proceed: ").lower().strip()
        match Option:
            case "1" | "add products" | "addproducts" | "add":
                AddProducts(Inventory, "", 0, 0)
            case "2" | "search" | "search product" | "ask for product" | "searchproduct" | "ask":
                AskProductsDetails("", Inventory)
            case "3" | "uptadate product" | "update" | "updateproduct":
                UpdateProductInfo()
            case "4" | "delete" | "delproduct" | "delete product" | "deleteproduct" | "del":
                DelProduct(Inventory)
            case "5" | "total" | "total value" | "totalvalue":
                TotalValue(Inventory)
            case "6" | "show" | "showfullinventory" | "show full":
                FullInventory()
            case "7" | "exit" | "end" | "finish" | "close":
                print("------------------------------------------")
                print("\033[1;31mExiting...\033[0m")
                print("------------------------------------------")
                break
            case _:
                print("------------------------------------------")
                print("\033[1;31mInvalid option, please try again\033[0m")                 

Menu()
