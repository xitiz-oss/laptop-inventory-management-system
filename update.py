def update(laptop_name, existing_quantity, new_quantity, get_flag):
    with open("stock.txt", "r") as to_update:
        check_lines = to_update.readlines()

        if get_flag:
            selected_laptop = laptop_name
            for _ in check_lines:
                for i in range(0, len(check_lines) + 1):
                    if selected_laptop in check_lines[i - 1]:
                        check_lines[i - 1] = check_lines[i - 1].replace(str(existing_quantity), str(new_quantity))

                with open("stock.txt", "w") as added_stock:
                    added_stock.writelines(check_lines)

        elif not get_flag:
            for _ in check_lines:
                selected_laptop = laptop_name
                for i in range(0, len(check_lines)):
                    if selected_laptop in check_lines[i - 1]:
                        check_lines[i - 1] = check_lines[i - 1].replace(str(existing_quantity), str(new_quantity))

            with open("stock.txt", "w") as file_:
                file_.writelines(check_lines)
