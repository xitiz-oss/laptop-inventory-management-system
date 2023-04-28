# imports from other files as libraries
import read


# sell method through which the quantity for the laptops are calculated, stored and returned
def sell(laptop_sold, quantity_sold):
    """
    Calculates the quantity differential and stores the laptop name
    Returns the name of laptop, existing quantity, new updated quantity and flag

    Parameters:
        :param laptop_sold: ID of laptop sold
        :param quantity_sold: Quantity of laptop sold

    Type:
        :type laptop_sold: int
        :type quantity_sold int

    Returns:
        :return: laptop_name, temp, new_qty, flag_
    """
    flag_ = False

    # storing the  existing value in a temp variable
    temp = read.read()[laptop_sold - 1][3]

    # storing the new quantity after calculation
    new_qty = int(read.read()[laptop_sold - 1][3]) - quantity_sold

    # accessing the name of the laptop
    laptop_name = read.read()[laptop_sold - 1][0]

    return laptop_name, temp, new_qty, flag_
