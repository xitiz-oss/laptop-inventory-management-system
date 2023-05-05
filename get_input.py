# imports from other files as libraries
import operations
import read


# get_buy_details methods prompts for all the details and returns the appropriate values when returned along with
# condition checking
def get_buy_details():
    """
    Admin can choose from various manufacturers and choose the desired laptop and respective quantity from the manufacturer
    Returns the laptop name, manufacturer, quantity bought, price of laptop, cpu and gpu of laptop

    Returns:
        :return: laptop_name, manufacturer, quantity, price, cpu, gpu

        If manufacturer is 'Lenovo', lenovo[0][0], manufacturer_chosen, quantity_chosen, lenovo[0][1], lenovo[0][2], lenovo[0][3] is returned
        Else if manufacturer is 'Razer', razer[0], manufacturer_chosen, quantity_chosen, razer[1], razer[2], razer[3] is returned
        Else if manufacturer is 'Dell', dell[0][0], manufacturer_chosen, quantity_chosen, dell[0][1], dell[0][2], dell[0][3] is returned
        Else if manufacturer is 'Alienware', alienware[0], manufacturer_chosen, quantity_chosen, alienware[1], alienware[2], alienware[3] is returned
        Else if manufacturer is 'Acer', acer[0][0], manufacturer_chosen, quantity_chosen, acer[0][1], acer[0][2], acer[0][3] is returned
        Else if manufacturer is 'Apple', apple[0][0], manufacturer_chosen, quantity_chosen, apple[0][1], apple[0][2], apple[0][3] is returned

    """
    # creating an infinite loop scenario along with exception handling to re-prompt if any invalid input is provided
    while True:
        # usage of try block to catch exceptions and handle them correctly
        try:
            print()
            # list of manufacturers
            manufacturers = ["Lenovo", "Razer", "Dell", "Alienware", "Acer", "Apple"]
            print("You can buy from the following manufacturers: ")

            # displaying available manufacturers
            for i in range(len(manufacturers)):
                print(f"{i + 1}) {manufacturers[i]}")

            print()
            print("Enter the name of manufacturer to buy from")
            manufacturer_chosen = input(">>> ").title().rstrip().lstrip()
            operations.exit_on_will(manufacturer_chosen)

            # validating the choice of manufacturer chosen from the available manufacturers
            while manufacturer_chosen not in manufacturers:
                print("INVALID INPUT \nSELECT FROM THE GIVEN NAMES OF MANUFACTURER")
                print()
                print("Enter the name of manufacturer to buy from")
                manufacturer_chosen = input(">>> ").title().rstrip().lstrip()
                operations.exit_on_will(manufacturer_chosen)

            # executable code for when 'lenovo' is chosen as the manufacturer
            if manufacturer_chosen == "Lenovo":
                # 2D list storing lenovo laptop details
                lenovo = [["Thinkpad", 1500, "i7 9th Gen", "No GPU"],
                          ["Lenovo Legion Pro", 1900, "i9 9th Gen", "GTX 3080"],
                          ["YOGA", 1300, "i5 9th Gen", "GTX 3050"]]
                print('''
                    ██      ███████ ███    ██  ██████  ██    ██  ██████  
                    ██      ██      ████   ██ ██    ██ ██    ██ ██    ██ 
                    ██      █████   ██ ██  ██ ██    ██ ██    ██ ██    ██ 
                    ██      ██      ██  ██ ██ ██    ██  ██  ██  ██    ██ 
                    ███████ ███████ ██   ████  ██████    ████    ██████          
                ''')
                print()
                print(f"{manufacturer_chosen} has following laptops: ")
                # iterating over the 2D list to display the available laptops
                for a in range(len(lenovo)):
                    print("=" * 40)
                    print(f"{a + 1}) Name: {lenovo[a][0]} \n \tProcessor: {lenovo[a][2]}  \n \tGraphics: {lenovo[a][3]} \n \tPrice: {lenovo[a][1]}")
                    print("=" * 40)

                print()
                print("Enter the laptop id you want to buy: ")
                while True:
                    # usage of try-except block to handle the exceptions correctly
                    try:
                        lenovo_chosen = int(input(">>> "))
                        print("Enter quantity:")
                        quantity_chosen = int(input(">>>"))
                        while True:
                            # returning the respective values as per the selection made
                            if quantity_chosen <= 0:
                                print("Re-Enter quantity:")
                                quantity_chosen = int(input(">>>"))

                            elif lenovo_chosen == 1:
                                return lenovo[0][0], manufacturer_chosen, quantity_chosen, lenovo[0][1], lenovo[0][2], lenovo[0][3]

                            elif lenovo_chosen == 2:
                                return lenovo[1][0], manufacturer_chosen, quantity_chosen, lenovo[1][1], lenovo[1][2], lenovo[1][3]

                            elif lenovo_chosen == 3:
                                return lenovo[2][0], manufacturer_chosen, quantity_chosen, lenovo[2][1], lenovo[2][2], lenovo[2][3]

                            elif lenovo_chosen > 3 or lenovo_chosen <= 0:
                                print()
                                print("INVALID INPUT FOR CHOICE")
                                print()
                                print("Enter again: ")
                                lenovo_chosen = int(input(">>> "))
                                print("Enter quantity:")
                                quantity_chosen = int(input(">>>"))

                    except ValueError:
                        print("ERROR \nENTER A INTEGER")

            # executable code for when 'razer' chosen as the manufacturer
            elif manufacturer_chosen == "Razer":
                razer = ["Razer Blade", 3000, "i7 7th Gen", "GTX 3070"]
                print('''
                        ██████   █████  ███████ ███████ ██████  
                        ██   ██ ██   ██    ███  ██      ██   ██ 
                        ██████  ███████   ███   █████   ██████  
                        ██   ██ ██   ██  ███    ██      ██   ██ 
                        ██   ██ ██   ██ ███████ ███████ ██   ██ 
                        ''')
                print()
                print(f"{manufacturer_chosen} has following laptops: ")
                print("=" * 40)
                print(f"1) Name: {razer[0]} \n \tProcessor: {razer[2]}  \n \tGraphics: {razer[3]} \n \tPrice: {razer[1]}")
                print("=" * 40)
                print()
                print("Enter the laptop id you want to buy: ")
                while True:
                    # usage of try-except block to handle the exceptions correctly
                    try:
                        razer_chosen = int(input(">>> "))
                        print("Enter quantity:")
                        quantity_chosen = int(input(">>>"))
                        while True:
                            # returning the respective values as per the selection made
                            if quantity_chosen <= 0:
                                print("Re-Enter quantity:")
                                quantity_chosen = int(input(">>>"))

                            elif razer_chosen == 1:
                                return razer[0], manufacturer_chosen, quantity_chosen, razer[1], razer[2], razer[3]

                            elif razer_chosen > 1 or razer_chosen <= 0:
                                print()
                                print("INVALID INPUT FOR CHOICE")
                                print()
                                print("Enter again: ")
                                razer_chosen = int(input(">>> "))
                                print("Enter quantity:")
                                quantity_chosen = int(input(">>>"))

                    except ValueError:
                        print("ERROR \nENTER A INTEGER")

            # executable code for when 'dell' chosen as the manufacturer
            elif manufacturer_chosen == "Dell":
                dell = [["XPS", 1200, "i5 5th Gen", "GTX 3060"], ["Inspiron", 1000, "i5 9th Gen", "No GPU"]]
                print('''
                    ██████  ███████ ██      ██      
                    ██   ██ ██      ██      ██      
                    ██   ██ █████   ██      ██      
                    ██   ██ ██      ██      ██      
                    ██████  ███████ ███████ ███████ 
                      ''')
                print()
                print(f"{manufacturer_chosen} has following laptops: ")

                for a in range(len(dell)):
                    print("=" * 40)
                    print(f"{a + 1}) Name: {dell[a][0]} \n \tProcessor: {dell[a][2]}  \n \tGraphics: {dell[a][3]} \n \tPrice: {dell[a][1]}")
                    print("=" * 40)

                print()
                print("Enter the laptop id you want to buy: ")
                while True:
                    # usage of try-except block to handle the exceptions correctly
                    try:
                        dell_chosen = int(input(">>> "))
                        print("Enter quantity:")
                        quantity_chosen = int(input(">>>"))
                        while True:
                            # returning the respective values as per the selection made
                            if quantity_chosen <= 0:
                                print("Re-Enter quantity:")
                                quantity_chosen = int(input(">>>"))

                            elif dell_chosen == 1:
                                return dell[0][0], manufacturer_chosen, quantity_chosen, dell[0][1], dell[0][2], dell[0][3]

                            elif dell_chosen == 2:
                                return dell[1][0], manufacturer_chosen, quantity_chosen, dell[1][1], dell[1][2], dell[1][3]

                            elif dell_chosen > 1 or dell_chosen <= 0:
                                print()
                                print("INVALID INPUT FOR CHOICE")
                                print()
                                print("Enter again: ")
                                dell_chosen = int(input(">>> "))
                                print("Enter quantity:")
                                quantity_chosen = int(input(">>>"))

                    except ValueError:
                        print("ERROR \nENTER A INTEGER")

            # executable code for when 'lenovo' ios chosen as the manufacturer
            elif manufacturer_chosen == "Alienware":
                alienware = ["Alienware", 1800, "i9 9th Gen", "GTX 3060"]
                print('''     
                 █████  ██      ██ ███████ ███    ██ ██     ██  █████  ██████  ███████ 
                ██   ██ ██      ██ ██      ████   ██ ██     ██ ██   ██ ██   ██ ██      
                ███████ ██      ██ █████   ██ ██  ██ ██  █  ██ ███████ ██████  █████   
                ██   ██ ██      ██ ██      ██  ██ ██ ██ ███ ██ ██   ██ ██   ██ ██      
                ██   ██ ███████ ██ ███████ ██   ████  ███ ███  ██   ██ ██   ██ ███████ 
                ''')
                print()
                print(f"{manufacturer_chosen} has following laptops: ")
                print("=" * 40)
                print(f"1) Name: {alienware[0]} \n \tProcessor: {alienware[2]}  \n \tGraphics: {alienware[3]} \n \tPrice: {alienware[1]}")
                print("=" * 40)
                print()
                print("Enter the laptop id you want to buy: ")
                while True:
                    # usage of try-except block to handle the exceptions correctly
                    try:
                        alienware_chosen = int(input(">>> "))
                        print("Enter quantity:")
                        quantity_chosen = int(input(">>>"))
                        while True:
                            # returning the respective values as per the selection made
                            if quantity_chosen <= 0:
                                print("Re-Enter quantity:")
                                quantity_chosen = int(input(">>>"))

                            elif alienware_chosen == 1:
                                return alienware[0], manufacturer_chosen, quantity_chosen, alienware[1], alienware[2], alienware[3]

                            elif alienware_chosen > 1 or alienware_chosen <= 0:
                                print()
                                print("INVALID INPUT FOR CHOICE")
                                print()
                                print("Enter again: ")
                                alienware_chosen = int(input(">>> "))
                                print("Enter quantity:")
                                quantity_chosen = int(input(">>>"))

                    except ValueError:
                        print("ERROR \nENTER A INTEGER")

            # executable code for when 'lenovo' ios chosen as the manufacturer
            elif manufacturer_chosen == "Acer":
                acer = [["Swift 7", 1000, "i5 9th Gen", "GTX 3060"],
                        ["Predator", 1900, "i9 9th Gen", "GTX 3080"]]
                print('''
                 █████   ██████ ███████ ██████  
                ██   ██ ██      ██      ██   ██ 
                ███████ ██      █████   ██████  
                ██   ██ ██      ██      ██   ██ 
                ██   ██  ██████ ███████ ██   ██
                ''')
                print()
                print(f"{manufacturer_chosen} has following laptops: ")
                # iterating over the 2D list to display the available laptops
                for a in range(len(acer)):
                    print("=" * 40)
                    print(f"{a + 1}) Name: {acer[a][0]} \n \tProcessor: {acer[a][2]}  \n \tGraphics: {acer[a][3]} \n \tPrice: {acer[a][1]}")
                    print("=" * 40)
                print()
                print("Enter the laptop id you want to buy: ")
                while True:
                    # usage of try-except block to handle the exceptions correctly
                    try:
                        acer_chosen = int(input(">>> "))
                        print("Enter quantity:")
                        quantity_chosen = int(input(">>>"))
                        while True:
                            # returning the respective values as per the selection made
                            if quantity_chosen <= 0:
                                print("Re-Enter quantity:")
                                quantity_chosen = int(input(">>>"))
                            elif acer_chosen == 1:
                                return acer[0][0], manufacturer_chosen, quantity_chosen, acer[0][1], acer[0][2], acer[0][3]

                            elif acer_chosen == 2:
                                return acer[1][0], manufacturer_chosen, quantity_chosen, acer[1][1], acer[1][2], acer[1][3]

                            elif acer_chosen > 2 or acer_chosen <= 0:
                                print()
                                print("INVALID INPUT FOR CHOICE")
                                print()
                                print("Enter again: ")
                                acer_chosen = int(input(">>> "))
                                print("Enter quantity:")
                                quantity_chosen = int(input(">>>"))

                    except ValueError:
                        print("ERROR \nENTER A INTEGER")

            # executable code for when 'lenovo' ios chosen as the manufacturer
            elif manufacturer_chosen == "Apple":
                apple = [["Macbook Pro 16", 3200, "M1 Pro", "Ten Core GPU"],
                         ["Macbook Air 13", 2200, "M1 Pro", "Ten Core GPU"]]
                print('''
                 █████  ██████  ██████  ██      ███████ 
                ██   ██ ██   ██ ██   ██ ██      ██      
                ███████ ██████  ██████  ██      █████   
                ██   ██ ██      ██      ██      ██      
                ██   ██ ██      ██      ███████ ███████ 
                ''')
                print()
                print(f"{manufacturer_chosen} has following laptops: ")
                # iterating over the 2D list to display the available laptops
                for a in range(len(apple)):
                    print("=" * 40)
                    print(f"{a + 1}) Name: {apple[a][0]} \n \tProcessor: {apple[a][2]}  \n \tGraphics: {apple[a][3]} \n \tPrice: {apple[a][1]}")
                    print("=" * 40)

                print()
                print("Enter the laptop id you want to buy: ")
                while True:
                    # usage of try-except block to handle the exceptions correctly
                    try:
                        apple_chosen = int(input(">>> "))
                        print("Enter quantity:")
                        quantity_chosen = int(input(">>>"))
                        while True:
                            # returning the respective values as per the selection made
                            if quantity_chosen <= 0:
                                print("Re-Enter quantity:")
                                quantity_chosen = int(input(">>>"))
                            elif apple_chosen == 1:
                                return apple[0][0], manufacturer_chosen, quantity_chosen, apple[0][1], apple[0][2], apple[0][3]

                            elif apple_chosen == 2:
                                return apple[1][0], manufacturer_chosen, quantity_chosen, apple[1][1], apple[1][2], apple[1][3]

                            elif apple_chosen > 1 or apple_chosen <= 0:
                                print()
                                print("INVALID INPUT FOR CHOICE")
                                print()
                                print("Enter again: ")
                                apple_chosen = int(input(">>> "))
                                print("Enter quantity:")
                                quantity_chosen = int(input(">>>"))

                    except ValueError:
                        print("ERROR \nENTER A INTEGER")
        except ValueError:
            print("INVALID INPUT")
        else:
            break


# get_info method where administrator enters detail of the customer and the laptop being sold
def get_info(customer_name):
    """
    Admin enters the name of the customer and the choice of the laptop of customer such that the admin can sell the laptop to the customer
    Returns the buy id of laptop, quantity bought by the customer, customer name

    Parameters:
        :param customer_name: Name of the customer

    Type:
        :type customer_name: str

    Returns:
        :return: item_buy, quantity_buy, customer_name
    """

    # displaying laptops to show the id of laptops
    for i in range(len(read.read())):
        print(f"{i + 1})->{read.read()[i][0]}", end=" \t\t")
    print()

    # creating an infinite loop scenario along with exception handling to re-prompt if any invalid input is provided
    while True:
        # usage of try-except block to handle the exceptions correctly
        try:
            print(f"Enter {customer_name}'s choice: ")
            item_buy = int(input(">>>"))
            print()

            print(f"Enter the no. of laptops chosen by {customer_name} ")
            quantity_buy = int(input(">>>"))
            print()

            while True:
                # validating the input provided within the loop such that for any invalid/inappropriate input, it can be re-prompted
                # which ensure the correct flow of thw system
                if item_buy > len(read.read()) or item_buy <= 0:
                    print("x__ERROR__x")
                    print("Choice is out of range")
                    print()
                    print(f"Enter {customer_name}'s choice: ")
                    item_buy = int(input(">>>"))
                    print(f"Enter the no. of laptops chosen by {customer_name} ")
                    quantity_buy = int(input(">>>"))

                elif quantity_buy <= 0:
                    print("x__ERROR__x")
                    print("Enter Valid Quantity")
                    print()
                    print(f"Enter the no. of laptops chosen by {customer_name} ")
                    quantity_buy = int(input(">>>"))

                elif (int(read.read()[item_buy - 1][3]) - quantity_buy) < 0:
                    print()
                    print("NOT ENOUGH STOCK! ")
                    print(f"We only have {read.read()[item_buy - 1][3]} {read.read()[item_buy - 1][0]} left...")
                    print("Please make your selection accordingly")
                    print()

                    operations.display()

                    print()
                    print("Re-enter selection")
                    print(f"Enter {customer_name}'s choice: ")
                    item_buy = int(input(">>>"))
                    print(f"Enter the no. of laptops chosen by {customer_name} ")
                    quantity_buy = int(input(">>>"))
                else:
                    break

        except ValueError:
            print("Not a valid integer! Enter again...")
        else:
            return item_buy, quantity_buy, customer_name
