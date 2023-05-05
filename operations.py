# imports from other files as libraries
import read


# display method to display all the available laptops from the stock file
def display():
    """
    Reads and unpacks the 2d list and the details are printed in a tabulated manner
    """
    display_specification = read.read()
    print("Following Laptops are available in our shop: ")
    print()
    print("=" * 143)
    print("| ITEM_NO \t|  AVAILABLE LAPTOPS IN SHOP \t| LAPTOP BRAND \t\t|  PRICE \t|  QUANTITY \t|  PROCESSOR \t| "
          "GRAPHICS IN LAPTOP  |")
    print("=" * 143)
    # iterating over the 2d list and unpacking it to display the laptops using len() to give a tabulated look
    for i in range(len(display_specification)):
        gpu_stripped = display_specification[i][5].replace('\n', '')
        print(f"| {i + 1})", " " * 9, " |", f" {display_specification[i][0]}", " " * (
                26 - (len(display_specification[i][0]))), " |", f" {display_specification[i][1]}", " " * (
                                     18 - (len(display_specification[i][1]))), " |", f" ${display_specification[i][2]}", " " * (
                                     9 - (len(display_specification[i][2]))), " |", f" {display_specification[i][3]}", " " * (
                                     10 - (len(str(display_specification[i][3])))), " |", f" {display_specification[i][4]}", " " * (
                                     10 - (len(display_specification[i][4]))), " |", f' {gpu_stripped}', " " * (
                                     16 - (len(gpu_stripped))), " |")
        print("-" * 143)
    print("=" * 143)
    print()


# function that takes input as parameter
# if the input entered is "exit" at any point of the program then the program ends
def exit_on_will(get_prompt):
    """
    Checks if the parameter is 'exit', and if so then the system is exited

    Parameters:
        :param get_prompt: any non-process input
    """
    if get_prompt == "exit":
        print("SYSTEM EXITING" + "." + "." + ".")
        print("EXITED")
        exit()


def get_customer_name():
    """
    Used to prompt the admin to enter the customer name, validates and returns customer name

    Returns:
    :return: customer_name
    """
    customer_name = input("Customer name: ").lstrip().rstrip()
    exit_on_will(customer_name)

    print()
    # usage of while loop to iterate if customer_name is not alphabetical characters
    while not customer_name.isalpha():
        print("Please enter a valid name and not an integer")
        print()
        customer_name = input("Customer name: ").lstrip().rstrip()
        exit_on_will(customer_name)

    return customer_name


def generate_structure(receipt_details, laptop_name, quantity_sold, laptop_price):
    """
    Generates a data structure under which the necessary details of the laptops sold are stored

    Parameters:
        :param receipt_details: List in which details are stored
        :param laptop_name: Name of the customer
        :param quantity_sold: Quantity of laptop sold
        :param laptop_price: Price of laptop sold

    Type:
        :type receipt_details: list
        :type laptop_name: str
        :type quantity_sold: int
        :type laptop_price: int

   Returns:
        :return: receipt_details
    """
    found_ = False

    # code to check if the laptop is already present in the stock file
    for detail_ in receipt_details:
        # if the laptop is found then the boolean found is set to be true
        if detail_[0] == laptop_name:
            detail_[1][0][1] += int(quantity_sold)
            found_ = True
            break

    if not found_:
        receipt_details.append([laptop_name,
                                [[laptop_price, quantity_sold]]])

    return receipt_details
