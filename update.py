# updating the file by directly accessing the file and replacing the values
def update(laptop_name, existing_quantity, new_quantity, get_flag):
    """
    Reads the file and depending upon the flag, the file is updated by replacing and writing over it

    Parameters:
        :param laptop_name: Name of the Laptop
        :param existing_quantity: Existing quantity of laptop in file
        :param new_quantity: New quantity of laptop to be updated in file
        :param get_flag: True if invoked from buy and False if invoked from sell

    Type:
        :type laptop_name: str
        :type existing_quantity: int
        :type new_quantity: int
        :type get_flag: bool

    """
    with open("stock.txt", "r") as to_update:
        check_lines = to_update.readlines()

        # get_flag = true for buying from manufacturers
        if get_flag:
            selected_laptop = laptop_name
            # iterating over the list
            for _ in check_lines:
                for i in range(0, len(check_lines) + 1):
                    # check if selected_laptop is present in the line at index i-1
                    # if the laptop is found, the code replaces the existing quantity in the line with a new quantity
                    if selected_laptop in check_lines[i - 1]:
                        check_lines[i - 1] = check_lines[i - 1].replace(str(existing_quantity), str(new_quantity))

                with open("stock.txt", "w") as added_stock:
                    # writelines writes the entire content of check_lines to the file
                    added_stock.writelines(check_lines)

        # get_flag = false for selling to customers
        elif not get_flag:
            # iterating over the list
            for _ in check_lines:
                selected_laptop = laptop_name
                for i in range(0, len(check_lines)):
                    # check if selected_laptop is present in the line at index i-1
                    # if the laptop is found, the code replaces the existing quantity in the line with a new quantity
                    if selected_laptop in check_lines[i - 1]:
                        check_lines[i - 1] = check_lines[i - 1].replace(str(existing_quantity), str(new_quantity))

            with open("stock.txt", "w") as file_:
                # writelines writes the entire content of check_lines to the file
                file_.writelines(check_lines)
