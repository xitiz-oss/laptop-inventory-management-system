import read


# sell method through which administrator enters detail of the customer and the laptop being sold and also call the
# method to generate receipt
def sell(laptop_sold, quantity_sold):
    flag_ = False

    # storing the  existing value in a temp variable
    temp = read.read()[laptop_sold - 1][3]

    # updating the quantity value in 2d list
    new_qty = int(read.read()[laptop_sold - 1][3]) - quantity_sold

    laptop_name = read.read()[laptop_sold - 1][0]

    return laptop_name, temp, new_qty, flag_
