import read


# buy method is called for the buying interface which updates the stock and also calls a method to generate the
# invoice for the purchase
def buy(bought_laptop_name, manufacturer, bought_laptop_qty, bought_laptop_price, chosen_cpu, chosen_gpu):
    flag_ = True

    vat = 0.13 * float(bought_laptop_price)

    with open("stock.txt", "r") as stock_file:
        check_lines = stock_file.readlines()
        availability_indication = False
        for line in check_lines:
            if bought_laptop_name in line:
                availability_indication = True
                break
            else:
                availability_indication = False

    if availability_indication:
        # storing the existing quantity
        updated_specifications = []
        with open("stock.txt", "r") as check_updated_stock:
            updated_lines = check_updated_stock.readlines()
            updated_lines = [line for line in updated_lines if line.strip()]

        for line in updated_lines:
            updated_specifications.append(line.split(", "))

        old_quantity = updated_specifications[read.get_line(bought_laptop_name, "stock.txt") - 1][3]
        # updating the existing quantity
        new_qty = int(updated_specifications[read.get_line(bought_laptop_name, "stock.txt") - 1][3]) + bought_laptop_qty

        return bought_laptop_name, manufacturer, bought_laptop_price, vat, old_quantity, new_qty, flag_

    else:
        with open("stock.txt", "a") as new_stock:
            new_stock.write(f"\n{bought_laptop_name}, {manufacturer}, {bought_laptop_price}, "
                            f"{bought_laptop_qty}, {chosen_cpu}, {chosen_gpu}")

        old_quantity = read.read()[read.get_line(bought_laptop_name, "stock.txt") - 1][3]
        # updating the existing quantity
        new_qty = int(read.read()[read.get_line(bought_laptop_name, "stock.txt") - 1][3]) + bought_laptop_qty

        return bought_laptop_name, manufacturer, bought_laptop_price, vat, old_quantity, new_qty, flag_
