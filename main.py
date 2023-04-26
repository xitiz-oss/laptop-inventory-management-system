import buy_from_distributor
import sell_to_customer
import get_input
import operations
import read
import update
import generation


# main method
def main():
    print("" + "=" * 25 + "\nx Welcome Administrator x\n" + "=" * 25)
    print()
    print('At any point if you would like to exit the system, please type "buyexit" ')
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
    operations.exit_on_will(buy_sell)
    print()
    while buy_sell not in ["buy", "sell"]:
        print("Administrator, Please enter 'Buy' or 'Sell'")
        buy_sell = input(">>>").lower().lstrip().rstrip()
        operations.exit_on_will(buy_sell)

    if buy_sell == "buy":
        read.invoice_details = []

        bought_laptop_name, manufacturer,bought_laptop_qty, bought_laptop_price,chosen_cpu, chosen_gpu  = get_input.get_buy_details()

        chosen_laptop_name, chosen_laptop_brand, chosen_laptop_price, vat, old_quantity, new_qty,flag_ = buy_from_distributor.buy(bought_laptop_name, manufacturer,bought_laptop_qty, bought_laptop_price,chosen_cpu, chosen_gpu)

        update.update(chosen_laptop_name, old_quantity, new_qty, flag_)

        while True:
            found = False
            for detail in read.invoice_details:
                if detail[0] == chosen_laptop_name:
                    detail[1][0][3] += int(bought_laptop_qty)
                    found = True
                    break

            if not found:
                read.invoice_details.append([chosen_laptop_name,
                                             [[chosen_laptop_brand, chosen_laptop_price, vat, bought_laptop_qty]]])

            # continuation prompt
            print("Would you like to continue exploring? (yes/no)")
            continuation = input(">>> ").lower().lstrip().rstrip()
            operations.exit_on_will(continuation)
            while continuation not in ["yes", "no"]:
                print("Not a Valid input! \nEnter yes or no")
                print("Would you like to continue buying? (yes/no)")
                continuation = input(">>>").lower().lstrip().rstrip()
                operations.exit_on_will(continuation)

            if continuation == "yes":
                bought_laptop_name, manufacturer, bought_laptop_qty, bought_laptop_price, chosen_cpu, chosen_gpu = \
                    get_input.get_buy_details()

                chosen_laptop_name, chosen_laptop_brand, chosen_laptop_price, vat, old_quantity, new_qty, \
                flag_ = buy_from_distributor.buy(bought_laptop_name, manufacturer, bought_laptop_qty,
                    bought_laptop_price, chosen_cpu, chosen_gpu)

                update.update(chosen_laptop_name, old_quantity, new_qty, flag_)
            else:
                # calling the generate_invoice method with provided arguments
                generation.generate_invoice(read.invoice_details)
                print("___The invoice has been generated___")
                print("Thank you for choosing XYZ Distributors.")
                print()

                break

    elif buy_sell == "sell":

        print("======================================")
        print("Shop's Selling Interface(Sell Laptops)")
        print("======================================")
        print()
        # calling the display method
        operations.display()

        laptop_sold, quantity_sold, name = get_input.get_info()
        laptop_name, temp, new_qty, flag_ = sell_to_customer.sell(laptop_sold, quantity_sold)

        update.update(laptop_name, temp, new_qty, flag_)

        generation.generate_receipt(laptop_sold, quantity_sold, name)

        # using while loop to create an infinite loop scenario unless the condition is fulfilled
        while True:
            print("Are there any other customers? (yes/no)")
            sell_continuation = input(">>> ").lower()
            operations.exit_on_will(sell_continuation)
            while sell_continuation not in ["yes", "no"]:
                print("Not a Valid input! \nEnter yes or no")
                print("Are there any other customers? (yes/no)")
                sell_continuation = input(">>> ").lower()
                operations.exit_on_will(sell_continuation)

            if sell_continuation == "yes":
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
    # asking the administrator for continuation in the interface
    print("Administrator, Would you like to return to the Shop's interface?")
    print('Enter "yes" or "no"')
    interface = input(">>>")
    operations.exit_on_will(interface)
    while True:
        while interface not in ["yes", "no"]:
            print("___ERROR___")
            print("UNCLEAR INSTRUCTIONS")
            print('Enter "yes" or "no"')
            interface = input(">>>")
            operations.exit_on_will(interface)
            if interface == "yes":
                main()
            else:
                print("SYSTEM EXITING" + "." + "." + ".")
                print("EXITED")
                break

        if interface == "yes":
            main()
            print("Administrator, Would you like to return to the Shop's interface?")
            print('Enter "yes" or "no"')
            interface = input(">>>")
            operations.exit_on_will(interface)
        else:
            print("SYSTEM EXITING" + "." + "." + ".")
            print("EXITED")
            break
