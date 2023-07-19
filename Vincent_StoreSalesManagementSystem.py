# >_____________________________________________________________________________________________________________________________________________< #
# --> product variable consist of each product data is inside a dictionary while each dictionary is inside a list.
# --> list index is then used as product id.
products = [{"name": "Bagel", "price": 55000.00, "quantity": 0, "segment": "Bakery", "sales": 30, "cogs": 25000.00},
            {"name": "Black Tea", "price": 27000.00, "quantity": 5, "segment": "Tea", "sales": 10, "cogs": 10000.00},
            {"name": "Bubble Tea", "price": 35000.00, "quantity": 10, "segment": "Tea", "sales": 90, "cogs": 12000.00},
            {"name": "Coffee", "price": 46000.00, "quantity": 15, "segment": "Coffee", "sales": 120, "cogs": 11000.00},
            {"name": "Croissant", "price": 57000.00, "quantity": 20, "segment": "Bakery", "sales": 50, "cogs": 30000.00},
            {"name": "Espressso", "price": 48000.00, "quantity": 25, "segment": "Coffee", "sales": 40, "cogs": 12000.00},
            {"name": "Green Tea", "price": 27000.00, "quantity": 30, "segment": "Tea", "sales": 20, "cogs": 9000.00},
            {"name": "Mocha", "price": 58000.00, "quantity": 35, "segment": "Coffee", "sales": 60, "cogs": 15000.00}]


# >_____________________________________________________________________________________________________________________________________________< #
# --> pin is nescessary for gaining access to report menu.
pin=123456



# >_____________________________________________________________________________________________________________________________________________< #
# --> def print_report(): is for printing a report
def print_report():
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Step 1: Printing products with its each product profit sorted from highest profit.
    sorted_products = sorted(products, key=lambda item:(item["price"] - item["cogs"]) * item["sales"], reverse=True)  
    print("List of products:")
    print(f"{'Rank':^5} {'Name':^25} {'Price':^10} {'Quantity':^8} {'Segment':^12} {'Sales':^8} {'CoGS':^10} {'Profit':^12}")
    for index, product in enumerate(sorted_products):
        print(f"{index + 1:>5} {product['name']:^25} {product['price']:>10} {product['quantity']:>8} {product['segment']:^12} {product['sales']:>8} {product['cogs']:>10} {(product['price']-product['cogs'])*product['sales']:>12}")
    print("")
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Step 2: Printing segment with its each segment profit sorted from highest profit.
    segment_profit = {}
    for product in products:
        segment = product["segment"]
        profit = (product["price"] - product["cogs"]) * product["sales"]
        if segment in segment_profit:
            segment_profit[segment] += profit
        else:
            segment_profit[segment] = profit
    sorted_segment_profit = dict(sorted(segment_profit.items(), key=lambda item: item[1], reverse=True))
    print("Segments Profit :")
    print(f"{'Rank':^5} {'Segment':^12} {'Profit':^12}")
    segmentid = 1
    for segment, profit in sorted_segment_profit.items():
        print(f"{segmentid:>5} {segment:^12} {profit:>12}")
        segmentid += 1
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Step 3: Printing Total Profit.        
    totalprofit=0
    for value in sorted_segment_profit.values():
        totalprofit+= value
    print(f"\n {'Total Profit':<17} {totalprofit:>12}\n")


# >_____________________________________________________________________________________________________________________________________________< #
# --> def print_all(): is for printing products without its cost of good sold.
def print_all():
    print("List of products:")
    print(f"{'id':^5} {'Name':^25} {'Price':^10} {'Quantity':^8} {'Segment':^12} {'Sales':^8}")    
    for index, product in enumerate(products):
        print(f"{index + 1:>5} {product['name']:^25} {product['price']:>10} {product['quantity']:>8} {product['segment']:^12} {product['sales']:>8}")
    print("")


# >_____________________________________________________________________________________________________________________________________________< #
# --> def print_reportid(p_id): is for printing a product limited only by requested product id.
def print_reportid(p_id):       
    print("Product Information: ")
    print(f"{'id':^5} {'Name':^25} {'Price':^10} {'Quantity':^8} {'Segment':^12} {'Sales':^8} {'CoGS':^10}")
    print(f"{p_id + 1:>5} {products[p_id]['name']:^25} {products[p_id]['price']:>10} {products[p_id]['quantity']:>8} {products[p_id]['segment']:^12} {products[p_id]['sales']:>8} {products[p_id]['cogs']:>10}\n")


# >_____________________________________________________________________________________________________________________________________________< #
# --> def print_id(p_id): is for printing a product without its cost of good sold limited only by requested product id.
def print_id(p_id):       
    print("Product Information: ")
    print(f"{'id':^5} {'Name':^25} {'Price':^10} {'Quantity':^8} {'Segment':^12} {'Sales':^8}")
    print(f"{p_id + 1:>5} {products[p_id]['name']:^25} {products[p_id]['price']:>10} {products[p_id]['quantity']:>8} {products[p_id]['segment']:^12} {products[p_id]['sales']:>8}\n")




# >_____________________________________________________________________________________________________________________________________________< #
# --> def read_products(): is for View Products Menu
def read_products():
    print("Welcome to View Products Menu")
    print("1. View all products")
    print("2. View a product")
    print("3. Exit to Main Menu")

    choice = input("Enter your choice (1-3): ")
    print(" ")
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 1: View all products. 
    if choice == "1":
        if not products:
            print("No products available.\n ")
            read_products()
        print_all()
        read_products()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 2: View a product based on requested product id. 
    elif choice == "2":
        if not products:
            print("No products available.\n ")
            read_products()

        p_id = int(input("Enter the product id: "))-1
        if 0 <= p_id < len(products):
            print_id(p_id)
            read_products()       
        else:
            print("Invalid product id.\n ")
            read_products()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 3: Exit to Main Menu. 
    elif choice == "3":
        main()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Else: Repeating View Products Menu. 
    else:
        print("Invalid choice. Please try again.\n ")
        read_products()


# >_____________________________________________________________________________________________________________________________________________< #
# --> def create_product(): is for Add Products Menu
def create_product():
    print("Welcome to Add Products Menu")
    print("1. Add a Product")
    print("2. Exit to Main Menu")

    choice = input("Enter your choice (1-2): ")
    print("")
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 1: Add a Product by entering name, price, quantity and segment while sales and cost of good sold are set as 0 by default. 
    if choice == "1":

        p_id = int(input(f"Enter the next product id (last id: {len(products)}): "))-1
        if 0 <= p_id < len(products):
            print("Data already exists\n ")
            create_product()
        elif p_id==len(products):
            name = input("Enter the product name: ").title()
            price = float(input("Enter the product price: "))
            quantity = int(input("Enter the initial stock quantity: "))
            segment = input("Enter the product segment: ").title()
            def create_save():
                save=input("Save Product Information (Y/N) ? : ").upper()
                if save=="Y":
                    products.append({"name": name, "price": price, "quantity": quantity, "segment": segment, "sales": 0, "cogs": 0})
                    print("Product added successfully!\n ")
                    create_product()
                elif save=="N":
                    create_product()
                else:
                    print("Invalid input. Please try again.\n ")
                    create_save()
            create_save()
        else:
            print("Invalid product id.\n ")
            create_product()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 2: Exit to Main Menu. 
    elif choice == "2":
        main()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Else: Repeating Add Products Menu. 
    else:
        print("Invalid choice. Please try again.\n ")
        create_product()


# >_____________________________________________________________________________________________________________________________________________< #
# --> def update_product(): is for Update Products Menu
def update_product():
    print("Welcome to Update Products Menu")
    print("1. Update a product")
    print("2. Exit to Main Menu")

    choice = input("Enter your choice (1-2): ")
    print(" ")
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 1: Update a product based on requested product id and category(price/quantity/sales). 
    if choice == "1":
        if not products:
            print("No products available.\n ")
            update_product()

        p_id = int(input("Enter the product id: "))-1
        if 0 <= p_id < len(products):
            print_id(p_id)
            def update_confirm():
                confirm=input("Continue Update (Y/N) ? : ").upper()
                if confirm=="Y":
                    def input_column():
                        column = input("Enter the name of product's column to update (price/quantity/sales) : ").lower()
                        if column in ["price"]:
                            newfloat = float(input(f"Enter the updated {column} :"))
                            def float_update():
                                floatupdate=input("Update Product Information (Y/N) ? : ").upper()
                                if floatupdate=="Y":
                                    products[p_id][column] = newfloat
                                    print("Product updated successfully!\n ")
                                    update_product()
                                elif floatupdate=="N":
                                    update_product()
                                else:
                                    print("Invalid input. Please try again.\n ")
                                    float_update()
                            float_update()
                        elif column in ["quantity","sales"]:
                            newint = int(input(f"Enter the updated {column} :"))
                            def int_update():
                                intupdate=input("Update Product Information (Y/N) ? : ").upper()
                                if intupdate=="Y":
                                    products[p_id][column] = newint
                                    print("Product updated successfully!\n ")
                                    update_product()
                                elif intupdate=="N":
                                    update_product()
                                else:
                                    print("Invalid input. Please try again.\n ")
                                    int_update()
                            int_update()                    
                        else:
                            print("Invalid input. Please try again.\n ")
                            input_column()
                    input_column()
                elif confirm=="N":
                    update_product()
                else:
                    print("Invalid input. Please try again.\n ")
                    update_confirm()
            update_confirm()
        else:
            print("Invalid product id.\n ")
            update_product()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 2: Exit to Main Menu. 
    elif choice == "2":
        main()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Else: Repeating Update Products Menu. 
    else:
        print("Invalid choice. Please try again.\n ")
        update_product()


# >_____________________________________________________________________________________________________________________________________________< #
# --> def delete_product(): is for Delete Products Menu
def delete_product():
    print("Welcome to Delete Products Menu")
    print("1. Delete a Product")
    print("2. Exit to Main Menu")

    choice = input("Enter your choice (1-2): ")
    print("")
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 1: Delete a product based on requested product id. 
    if choice == "1":
        if not products:
            print("No products available.\n ")
            delete_product()

        p_id = int(input(f"Enter product id : "))-1
        if 0 <= p_id < len(products):
            print_id(p_id)
            def delete_confirm():
                confirm=input("Delete the product (Y/N) ? : ").upper()
                if confirm=="Y":
                    deleted_product = products.pop(p_id)
                    print(f"{deleted_product['name']} successfully deleted\n ")
                    delete_product()
                elif confirm=="N":
                    delete_product()
                else:
                    print("Invalid input. Please try again.\n ")
                    delete_confirm()
            delete_confirm()
        else:
            print("Data does not exist\n ")
            delete_product()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 2: Exit to Main Menu. 
    elif choice == "2":
        main()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Else: Repeating Delete Products Menu. 
    else:
        print("Invalid choice. Please try again.\n ")
        delete_product()


# >_____________________________________________________________________________________________________________________________________________< #
# --> def record_sales(): is for Record Sales Menu
def record_sales():
    print("Welcome to Record Sales Menu")
    print("1. Record a Product Sales")
    print("2. Exit to Main Menu")

    choice = input("Enter your choice (1-2): ")
    print("")
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 1: Record sales of a product based on requested product id and reducing that product quantity. 
    if choice == "1":
        if not products:
            print("No products available.\n ")
            record_sales()

        p_id = int(input(f"Enter product id : "))-1
        if 0 <= p_id < len(products):
            print_id(p_id)
            def sales_confirm():
                confirm=input("Continue (Y/N) ? : ").upper()
                if confirm=="Y":
                    recordsales = int(input("Enter the quantity sold: "))
                    if 0<= recordsales <= products[p_id]["quantity"]:
                        products[p_id]["quantity"] -= recordsales
                        products[p_id]["sales"] += recordsales
                        print("Sales recorded successfully!\n ")
                        record_sales()
                    else:
                        print("Insufficient quantity or invalid input.\n ")
                        record_sales()
                elif confirm=="N":
                    record_sales()
                else:
                    print("Invalid input. Please try again.\n ")
                    sales_confirm()
            sales_confirm()
        else:
            print("Data does not exist\n ")
            record_sales()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 2: Exit to Main Menu. 
    elif choice == "2":
        main()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Else: Repeating Record Sales Menu. 
    else:
        print("Invalid choice. Please try again.\n ")
        record_sales()


# >_____________________________________________________________________________________________________________________________________________< #
# --> def report_menu(): is for Report Menu
def report_menu():
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Enter Pin to gain access
    access = int(input("Enter Pin (6 digits): "))
    if access == pin:
        def access_granted():
            print("Welcome to Report Menu")
            print("1. Make a report")
            print("2. Update a Product Cost of Good Sold")  
            print("3. Change Pin Numbers")
            print("4. Exit to Main Menu")

            choice = input("Enter your choice (1-4): ")
            print(" ")
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 1: Make a report by using print_report(). 
            if choice == "1":
                print_report()
                access_granted()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 2: Update a Product Cost of Good Sold based on requested product id
            elif choice == "2":
                if not products:
                    print("No products available.\n ")
                    access_granted()

                p_id = int(input("Enter the product id: "))-1
                if 0 <= p_id < len(products):
                    print_reportid(p_id)
                    def updatecogs_confirm():
                        confirm=input("Continue Update (Y/N) ? : ").upper()
                        if confirm=="Y":
                            newcogs = float(input(f"Enter the updated Cost of Good Sold :"))
                            def cogs_update():
                                cogsupdate=input("Update Product Information (Y/N) ? : ").upper()
                                if cogsupdate=="Y":
                                    products[p_id]["cogs"] = newcogs
                                    print("Product updated successfully!\n ")
                                    access_granted()
                                elif cogsupdate=="N":
                                    access_granted()
                                else:
                                    print("Invalid input. Please try again.\n ")
                                    cogs_update()
                            cogs_update()
                        elif confirm=="N":
                            access_granted()
                        else:
                            print("Invalid input. Please try again.\n ")
                            updatecogs_confirm()
                    updatecogs_confirm()
                else:
                    print("Invalid product id.\n ")
                    access_granted()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 3: Change Pin Numbers
            elif choice == "3":
                access = int(input("Enter Pin (6 digits): "))
                global pin
                if access == pin:
                    pin1 = int(input("Enter New Pin (6 digits): "))
                    pin2 = int(input("Reconfirm New Pin : "))
                    if pin1 == pin2:
                        pin = pin1
                        print("Pin Numbers changed successfully!\n ")
                    else:
                        print("Wrong Pin Numbers\n")
                        main()
                else:
                    print("Wrong Pin Numbers\n")
                    main()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Choice 4: Exit to Main Menu. 
            elif choice == "4":
                main()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Else: Repeating Report Menu after granted access.
            else:
                print("Invalid choice. Please try again.\n ")
                access_granted()
        access_granted()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Entering wrong Pin resulted in failing to gain access
    else:
        print("Wrong Pin Numbers\n")
        main()


# >_____________________________________________________________________________________________________________________________________________< #
# --> def main(): is for Main Menu
def main():
    while True:
        print("Welcome to Store Sales Management System")
        print("1. View Products")
        print("2. Add Products")
        print("3. Update Products")
        print("4. Delete Products")
        print("5. Record Sales")
        print("6. Report")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        print(" ")
        if choice == "1":
            read_products()
        elif choice == "2":
            create_product()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            record_sales()
        elif choice == "6":
            report_menu()
    # >-------------------------------------------------------------------------------------------------------------------------------------< #
    # --> Exit to terminate program        
        elif choice == "7":
            print("Goodbye and See You Next Time\n ")
            exit()
        else:
            print("Invalid choice. Please try again.\n ")
main()