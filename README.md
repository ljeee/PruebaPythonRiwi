# Req: Python and a debugger

### This is what the menu looks like
 Exit in this code is holy 

    ------------------------------------------
    Weclome to the inventory mangament system
    ------------------------------------------
    1. Add Products
    2. Search for product
    3. Update product info
    4. Delete product
    5. Total stock value
    6. Show Full Inventory
    7. Exit  End  Finish  Close
    ------------------------------------------
    Selec a option to proceed: 

### Chose a option introducing what you want to do, this menu accepts number or text

# Case 1 Add Products 
Then of introduced the option, he asks for the name
Then request a price and after request a quantity
at the final adds the details in the inventory

     --------------------------------------------------------
     Introduce the Product name: Mile                        
     --------------------------------------------------------
     Product Mile added                                      
     Introduce the price of the product: 100000.00           
     Price of Mile added                                     
     Enter the Product quantity: 1                           
     Quantity of Mile added                                  
     --------------------------------------------------------
     Product Mile added with Price $10000.00 and quantity: 10
     --------------------------------------------------------


# Case 2  Search product
This option search in the inventory according to the input
and search for the input in the inventory
then show if the product is in the list or not

     -------------------------------------------------------------------
     The Product Uwu is not in the inventory. Please try again or exit  
     -------------------------------------------------------------------
     Enter the name of the Product to search: Jefer                     
     -------------------------------------------------------------------
     The Product Jefer is not in the inventory. Please try again or exit
     ------------------------------------------------------------------
     Enter the name of the Product to search: Coke                      
     -------------------------------------------------------------------
     Product: Coke  Price: $20.30  Quantity: 3                        
     -------------------------------------------------------------------

# Case 3 Update product  
This option calls the full inventory and show the list of products
if is the inventory clear return to the menu ifnot he ask for
the name of the product what you want to change, validate the input
then ask you if you want to change the price or the quantity

    -------------------------------------------------------------------------------------
    This is the list of products in the inventory                                       
    -------------------------------------------------------------------------------------
    Product: Popcorn  Price: $5.10  Quantity: 10                                       
    Product: Coke  Price: $20.30  Quantity: 3                                          
    Product: Chocoramo  Price: $15.40  Quantity: 10                                    
    Product: Sparkies  Price: $1.00  Quantity: 30                                      
    Product: Lolete  Price: $0.00  Quantity: 1                                         
    ------------------------------------------------------------------------------------- 
    Enter the name of the product to update or type 'exit' to return to the menu: Lolete 
    What do you want to change? Price/Quantity: Price                                    
    What is the new price? 10000                                                         
    -------------------------------------------------------------------------------------
    The price of Lolete has been updated to 10000.00                                     
    -------------------------------------------------------------------------------------

# Case 4  Delete product
This option looks for coincidences between the name of the product
to eliminate and the items in the inventory if found coincides 
removes the item from the inventory

    ---------------------------------------------------------------------------------
    Inventory:                                                                       
    ---------------------------------------------------------------------------------
    -> Popcorn                                                                       
    -> Coke                                                                          
    -> Chocoramo                                                                     
    -> Sparkies                                                                      
    Enter the name of the product to delete or type exit to return to the menu: cok  
    ---------------------------------------------------------------------------------
    The product is not in the inventory. Please try again                            
    ---------------------------------------------------------------------------------
    Enter the name of the product to delete or type exit to return to the menu: Coke 
    ---------------------------------------------------------------------------------
    Product Coke removed                                                             
    ---------------------------------------------------------------------------------

# Case 5 Total Value 
First checks the status of the inventory if is empty he says it
if not applys the lamba funcition to the hole inventory and 
then shows the total value of inventory

    ------------------------------------------ 
    Total value of the inventory: $295.90    
    ------------------------------------------

# Case 6 Show Full Inventory 
This option reeds all the inventory if is empty he says it, if not
show you the hole inventory

    --------------------------------------------------
    This is the list of products in the inventory    
    --------------------------------------------------
    Product: Popcorn  Price: $5.10  Quantity: 10    
    Product: Coke  Price: $20.30  Quantity: 3       
    Product: Chocoramo  Price: $15.40  Quantity: 10 
    Product: Sparkies  Price: $1.00  Quantity: 30   
    Product: Lolete  Price: $0.00  Quantity: 1      
    --------------------------------------------------

# Case 7  Exit  End  Finish 
This option end the terminal :b

    ------------------------------------------
    Exiting........                           
    ------------------------------------------
