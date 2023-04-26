global invoice_details, quantity, item, settings, lines, flag, same_laptop_dict, order_and_quantity


def read():
    # opening a file to read
    with open("stock.txt", "r") as file:
        # readlines() returns a list of each line
        lines = file.readlines()
        lines = [line for line in lines if line.strip()]
        # empty list
        specifications_details = []
        # iterating to unpack the file and create the 2d list
        for each in lines:
            specifications_details.append(each.split(", "))
            file.seek(0, 2)

    return specifications_details


def get_line(phrase, file_name):
    with open(file_name, "r") as line_number:
        lines_number = line_number.readlines()
        lines_number = [line for line in lines_number if line.strip()]
        for i, line in enumerate(lines_number, 1):
            if phrase in line:
                return i
