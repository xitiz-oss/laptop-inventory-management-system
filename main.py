# imports from other files as libraries
import buy_from_distributor
import sell_to_customer
import get_input
import operations
import read
import update
import generation


# main method
def main():
    """
    Carries out all the tasks of the program
    Function invocation, Continuation, choosing operations are all carried out within main()
    The entire flow of program is based around main()
    """
    # shop details
    print("="*30)
    print("ByteBrew Technologies")
    print("="*30)
    print("Putalisadak, Kathmandu 44600")
    print("P.O BOX: 3314-24500")
    print("TEL: 01-534029")
    print("laptop_shop@gmail.com")
    print("="*30)
    print()
    
    print("=" * 25 + "\nx Welcome Administrator x\n" + "=" * 25)
    print()
    # entering "exit" at any time except for the middle of the program will exit the program and the data will be lost
    print('At any point if you would like to exit the system, please type "exit" ')
    print("=" * 5, "\n P.S.")
    print("=" * 5)
    print("Exiting the program mid-way will result in loss of the data")
    print()
    print("=" * 80)
    # prompting the administrator to either buy for shop or sell from shop
    print("Would you like to buy laptops for the Store or sell Laptops to customers?")
    print("=" * 80)
    print("Enter (buy/sell)")
    buy_sell = input(">>>").lower().lstrip().rstrip()
    # calling the exit_on_will method to check if "exit" phrase has been entered and if so then the program exits
    operations.exit_on_will(buy_sell)
    print()
    # checking for the input which cannot be anything else than 'buy or 'sell'
    # if wrong input entered then the admin is prompted again
    while buy_sell not in ["buy", "sell"]:
        print("Administrator, Please enter 'Buy' or 'Sell'")
        buy_sell = input(">>>").lower().lstrip().rstrip()
        operations.exit_on_will(buy_sell)

    if buy_sell == "buy":
        read.invoice_details = []

        # calling the get_buy_details method from get_input which returns the respective values and unpacks in the given variables
        bought_laptop_name, manufacturer, bought_laptop_qty, bought_laptop_price, chosen_cpu, chosen_gpu = get_input.get_buy_details()

        # calling the buy method from buy_from_distributor which returns the respective values and unpacks in the given variables
        chosen_laptop_name, chosen_laptop_brand, chosen_laptop_price, vat, old_quantity, new_qty, flag_ = buy_from_distributor.buy(bought_laptop_name, manufacturer, bought_laptop_qty, bought_laptop_price, chosen_cpu, chosen_gpu)

        # calling the update method from update which updates the file with the given parameters
        update.update(chosen_laptop_name, old_quantity, new_qty, flag_)

        # usage of while loop to create a fake loop scenario
        while True:
            found = False
            # code to check if the laptop is already present in the stock file
            for detail in read.invoice_details:
                # if the laptop is found then the boolean found is set to be true
                if detail[0] == chosen_laptop_name:
                    detail[1][0][3] += int(bought_laptop_qty)
                    found = True
                    break

            # if the boolean value false then the laptop is appears to be new and appends to the file
            if not found:
                read.invoice_details.append([chosen_laptop_name,
                                             [[chosen_laptop_brand, chosen_laptop_price, vat, bought_laptop_qty]]])

            # continuation prompt
            print("Would you like to continue exploring? (yes/no)")
            continuation = input(">>> ").lower().lstrip().rstrip()
            operations.exit_on_will(continuation)
            # input checking for  continuation prompt using while loop
            while continuation not in ["yes", "no"]:
                print("Not a Valid input! \nEnter yes or no")
                print("Would you like to continue buying? (yes/no)")
                continuation = input(">>>").lower().lstrip().rstrip()
                operations.exit_on_will(continuation)

            # if the admin continues to explore then the same procedure is followed by the invocation of respective function
            if continuation == "yes":
                bought_laptop_name, manufacturer, bought_laptop_qty, bought_laptop_price, chosen_cpu, chosen_gpu = get_input.get_buy_details()

                chosen_laptop_name, chosen_laptop_brand, chosen_laptop_price, vat, old_quantity, new_qty, flag_ = buy_from_distributor.buy(bought_laptop_name, manufacturer, bought_laptop_qty, bought_laptop_price, chosen_cpu, chosen_gpu)

                update.update(chosen_laptop_name, old_quantity, new_qty, flag_)
            else:
                # calling the generate_invoice method with provided arguments
                generation.generate_invoice(read.invoice_details)
                print("___The invoice has been generated___")
                print("Thank you for choosing XYZ Distributors.")
                print()
                break

    elif buy_sell == "sell":
        # entering the shops interface to sell the laptops to the customer
        print("======================================")
        print("Shop's Selling Interface(Sell Laptops)")
        print("======================================")
        print()
        # calling the display method from operations which displays the available laptops in the stock file
        operations.display()

        # calling the get_info method from get_input which returns the respective values and unpacks in the given variables
        laptop_sold, quantity_sold, name = get_input.get_info()

        # calling the sell method from sell_to_customer which returns the respective values and unpacks in the given variables
        laptop_name, temp, new_qty, flag_ = sell_to_customer.sell(laptop_sold, quantity_sold)

        # calling the update method from update which updates the file with given parameters
        update.update(laptop_name, temp, new_qty, flag_)

        # calling the generate_receipt method to generate receipt for each laptop bought by the customer
        generation.generate_receipt(laptop_sold, quantity_sold, name)

        # using while loop to create an infinite loop scenario unless the condition is fulfilled
        while True:
            print("Are there any other customers? (yes/no)")
            # prompting to see if there are more customers to sell the laptops to
            sell_continuation = input(">>> ").lower().lstrip().rstrip()
            operations.exit_on_will(sell_continuation)
            # validating the input provided by the admin and re-prompt as per the condition
            while sell_continuation not in ["yes", "no"]:
                print("Not a Valid input! \nEnter yes or no")
                print("Are there any other customers? (yes/no)")
                sell_continuation = input(">>> ").lower().lstrip().rstrip()
                operations.exit_on_will(sell_continuation)

            if sell_continuation == "yes":
                # if the admin decides to continue then all the necessary methods required for selling are carried out
                operations.display()

                laptop_sold, quantity_sold, name = get_input.get_info()

                laptop_name, temp, new_qty, flag_ = sell_to_customer.sell(laptop_sold, quantity_sold)

                update.update(laptop_name, temp, new_qty, flag_)

                generation.generate_receipt(laptop_sold, quantity_sold, name)
            else:
                print("___The receipt has been generated___")
                break


if __name__ == "__main__":
    # calling main method
    main()
    print("Your stock has been updated")
    operations.display()
    # asking the administrator for continuation in the interface
    print("Administrator, Would you like to return to the Shop's interface?")
    print('Enter "yes" or "no"')
    interface = input(">>>").lower().lstrip().rstrip()
    operations.exit_on_will(interface)
    while True:
        # validating input from the admin to continue running the system
        while interface not in ["yes", "no"]:
            print("___ERROR___")
            print("UNCLEAR INSTRUCTIONS")
            print('Enter "yes" or "no"')
            interface = input(">>>").lower().lstrip().rstrip()
            operations.exit_on_will(interface)
            if interface == "yes":
                # calling main if the admin continues to run the system
                main()
            else:
                print("SYSTEM EXITING" + "." + "." + ".")
                print("EXITED")
                break

        if interface == "yes":
            main()
            print("Administrator, Would you like to return to the Shop's interface?")
            print('Enter "yes" or "no"')
            interface = input(">>>").lower().lstrip().rstrip()
            operations.exit_on_will(interface)
        else:
            print("SYSTEM EXITING" + "." + "." + ".")
            print("EXITED")
            break
