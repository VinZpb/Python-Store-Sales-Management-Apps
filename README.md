# Store Sales Management System #
  This program is python based and use for managing store sales data.
  The program is intended to be used by both employees and stakeholders.
  The employee can't gain access to confidential data while the stakeholder gains access to all data.


# --> Data Storage
- products variable consist of each product data is inside a dictionary while each dictionary is inside a list.
- list index is then used as product id.

# --> Main menu is consist of 7 option as presented:
Welcome to Store Sales Management System
1. View Products         
2. Add Products            # --> Add a Product by entering name, price, quantity and segment while sales and cost of good sold are set as 0 by default.
3. Update Products         # --> Update a product based on requested product id and category(price/quantity/sales).
4. Delete Products         # --> Delete a product based on requested product id.
5. Record Sales            # --> Record sales of a product based on requested product id and reducing that product quantity.
6. Report                  # --> Pin is necessary for gaining access to report menu. Cost of Good Sold of products can only be viewed and updated in this menu.
7. Exit                    # --> Exit to terminate program 

# --> Views menu is consist of 3 option as presented:
Welcome to View Products Menu
1. View all products
2. View a product           # --> View a product based on requested product id.
3. Exit to Main Menu

# --> Add products menu is consist of 2 option as presented:
Welcome to Add Products Menu
1. Add a Product
2. Exit to Main Menu

# --> Update products menu is consist of 2 option as presented:
Welcome to Update Products Menu
1. Update a product
2. Exit to Main Menu

# --> Delete products menu is consist of 2 option as presented:
Welcome to Delete Products Menu
1. Delete a Product
2. Exit to Main Menu

# --> Record sales menu is consist of 2 option as presented:
Welcome to Record Sales Menu
1. Record a Product Sales
2. Exit to Main Menu

# --> Report menu is consist of 4 option as presented:
Welcome to Report Menu
1. Make a report                          # --> Consist of 3 steps as follows:
                                                # --> Step 1: Printing products with its each product profit sorted from highest profit.
                                                # --> Step 2: Printing segment with its each segment profit sorted from highest profit.
                                                # --> Step 3: Printing Total Profit.   
2. Update a Product Cost of Good Sold     # --> Update a Product Cost of Good Sold based on requested product id
3. Change Pin Numbers
4. Exit to Main Menu
