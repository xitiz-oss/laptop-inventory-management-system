# global variables declaration
global invoice_details, receipt_details, quantity, item, lines, flag, order_and_quantity


# function which reads the original stock file
def read():
    """
    Reads the file and converts the details into 2d list
    Returns the 2d list of laptop details

    Returns:
        :return: specifications_details
    """
    # opening a file to read
    with open("stock.txt", "r") as file:
        # readlines() returns a list of each line
        lines = file.readlines()
        # checks for any blank line and if any present then it is stripped away
        lines = [line for line in lines if line.strip()]
        # empty list
        specifications_details = []
        # iterating to unpack the file and create the 2d list
        for each in lines:
            specifications_details.append(each.split(", "))

    return specifications_details


# function to match the name of the laptop and provide its line number in the file
def get_line(phrase, file_name):
    """
    Reads the file and enumerates over the lines to check for the laptop name provided as parameter
    When the name is found in a line, then the line number is returned

    Parameters:
        :param phrase: Name of the laptop
        :param file_name: File to check

    Returns:
        :return: i
    """
    # file opened to read
    with open(file_name, "r") as line_number:
        # each line read as lists
        lines_number = line_number.readlines()
        # stripping away if any blank lines is present
        lines_number = [line for line in lines_number if line.strip()]
        # enumerate functions acts as a provider for counter for what we are iterating through
        for i, line in enumerate(lines_number, 1):
            # if the name provided is present in a given line, then the value of i or line number is returned
            if phrase in line:
                return i
