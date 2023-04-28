# imports from other files as libraries
import read


# buy method is called for the buying interface which updates the stock which are bought from the manufacturers
def buy(bought_laptop_name, manufacturer, bought_laptop_qty, bought_laptop_price, chosen_cpu, chosen_gpu):
    """
    Checks the availability of laptop in the stock file, if available values are returned, else the details are written on the file and only then returned matching that line
    Returns the laptop name chosen, manufacturer, existing quantity, calculated quantity, price, calculated vat and flag

    Parameters:
        :param bought_laptop_name: Name of the laptop bought
        :param manufacturer: Manufacturer of the laptop bought
        :param bought_laptop_price: Price of the laptop bought
        :param chosen_cpu: CPU of the laptop bought
        :param chosen_gpu: GPU of the laptop bought

    Type:
        :type bought_laptop_name: str
        :type manufacturer: str
        :type bought_laptop_qty: int
        :type bought_laptop_price: int
        :type chosen_cpu: str
        :type chosen_gpu: str


    Returns:
        :return: bought_laptop_name, manufacturer, bought_laptop_price, vat, old_quantity, new_qty, flag_

    """
    flag_ = True

    # calculating vat
    vat = 0.13 * float(bought_laptop_price)

    with open("stock.txt", "r") as stock_file:
        check_lines = stock_file.readlines()
        availability_indication = False
        for line in check_lines:
            # checks the laptop name line by line and if found then the availability indication is set to be true
            if bought_laptop_name in line:
                availability_indication = True
                break
            # else the availability indication is set to be false
            else:
                availability_indication = False

    # for availability indication being true
    if availability_indication:
        # empty list
        updated_specifications = []
        with open("stock.txt", "r") as check_updated_stock:
            updated_lines = check_updated_stock.readlines()
            # stripping the lines for any blank lines
            updated_lines = [line for line in updated_lines if line.strip()]

        for line in updated_lines:
            updated_specifications.append(line.split(", "))

        # the get_line method from reads is used to access the line number for the laptop in the file
        # storing the existing quantity
        old_quantity = updated_specifications[read.get_line(bought_laptop_name, "stock.txt") - 1][3]
        # updating the existing quantity
        new_qty = int(updated_specifications[read.get_line(bought_laptop_name, "stock.txt") - 1][3]) + bought_laptop_qty

        return bought_laptop_name, manufacturer, bought_laptop_price, vat, old_quantity, new_qty, flag_

    else:
        # for availability indication being false the file is opened in append mode
        # then the new laptop is appended to the file
        with open("stock.txt", "a") as new_stock:
            new_stock.write(f"\n{bought_laptop_name}, {manufacturer}, {bought_laptop_price}, "
                            f"{bought_laptop_qty}, {chosen_cpu}, {chosen_gpu}")

        # the get_line method from reads is used to access the line number for the laptop in the file
        # storing the existing quantity
        old_quantity = read.read()[read.get_line(bought_laptop_name, "stock.txt") - 1][3]
        # updating the existing quantity
        new_qty = int(read.read()[read.get_line(bought_laptop_name, "stock.txt") - 1][3]) + bought_laptop_qty

        return bought_laptop_name, manufacturer, bought_laptop_price, vat, old_quantity, new_qty, flag_
