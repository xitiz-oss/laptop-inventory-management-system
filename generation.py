# imports from other files as libraries
from datetime import datetime
import read


# generate_invoice creates the invoice for the laptops bought by the administrator for the shop
def generate_invoice(invoice_details):
    """
    When invoked, all the details regarding the buying part is unpacked to generate an invoice on file as well as by printing on console

    Parameters:
        :param invoice_details: list containing details about bought laptop

    Type:
        :type invoice_details: list

    """
    # using the datetime class the current date and time
    now = datetime.now()

    total_price = 0
    total_vat = 0

    # creating a unique file which does not pre-exist in Invoice folder using relative path
    _ = open(f"./Invoices/SHOP_({now.day}|{now.month}|{now.year})_({now.hour}:{now.minute}:{now.second}).txt", "x")



    # opening the file to write and generating the invoice
    with open(f"./Invoices/SHOP_({now.day}|{now.month}|{now.year})_({now.hour}:{now.minute}:{now.second}).txt", "w") as invoice:
        invoice.write("========================================================= \n")
        invoice.write(f"                       INVOICE \n")
        invoice.write("========================================================= \n")
        invoice.write("--Automated--\n")
        invoice.write("\n")
        invoice.write("\n")
        invoice.write(f"Bought by: ByteBrew Technologies\n")
        invoice.write("========================================================= \n")
        invoice.write(f"Served by: Admin\n")
        invoice.write("\n")
        invoice.write("\n")
        invoice.write("Laptops bought:\n")
        invoice.write("--------------------------------------------------------- \n")
        invoice.write("| NAME \t\t\t| BRAND \t| QUANTITY \t|\n")
        invoice.write("--------------------------------------------------------- \n")
        for details in invoice_details:
            name = details[0]
            # details[1] is actually a list stored within the 2D list
            item_details = details[1]
            for item_ in item_details:
                # unpacking each value to store in the variables
                item_brand, item_price, item_vat, item_quantity = item_
                total_price += item_price
                total_vat += item_vat
                # writing the details in a tabulated manner
                invoice.write(f"| {name}" + " " * (21 - len(str(name))) + " |" + f" {item_brand}" + " " * (
                        13 - len(item_brand)) + " |" + f" {item_quantity}" + " " * (
                                      13 - len(str(item_quantity))) + " |\n")
        invoice.write("--------------------------------------------------------- \n")
        invoice.write("\n")
        invoice.write(f" {str(now)} \n")
        invoice.write("--------------------------------------------------------- \n")
        invoice.write(f"                                   Price: ${total_price} \n")
        invoice.write(f"                                     VAT: ${round(total_vat, 1)} \n")
        invoice.write(f"                            Gross amount: ${total_price + total_vat}\n")
        invoice.write("--------------------------------------------------------- \n")
        invoice.write("                      x THANK YOU x \n")
        invoice.write("========================================================= \n")

    # invoice printed on console
    print("========================================================= ")
    print(f"                        INVOICE ")
    print("========================================================= ")
    print("--Automated-- ")
    print()
    print("Bought by: ByteBrew Technologies")
    print("========================================================= ")
    print(f"Served by: Admin")
    print()
    print("Laptops bought:")
    print("--------------------------------------------------------- ")
    print("| NAME \t\t\t| BRAND \t| QUANTITY \t|")
    print("--------------------------------------------------------- ")
    for details in invoice_details:
        name = details[0]
        # details[1] is actually a list stored within the 2D list
        item_details = details[1]
        for item_ in item_details:
            # unpacking each value to store in the variables
            item_brand, item_price, item_vat, item_quantity = item_
            total_price += item_price
            total_vat += item_vat
            # printing the details in a tabulated manner
            print(f"| {name}", " " * (19 - len(str(name))), " |", f" {item_brand}", " " * (
                    10 - len(item_brand)), " |", f" {item_quantity}", " " * (10 - len(str(item_quantity))), " |")
    print("--------------------------------------------------------- ")
    print(f" {str(now)} ")
    print("--------------------------------------------------------- ")
    print(f"                                  Price: ${total_price} \n")
    print(f"                                    VAT: ${round(total_vat, 1)} \n")
    print(f"                           Gross amount: ${total_price + total_vat}\n")
    print("--------------------------------------------------------- ")
    print("                      x THANK YOU x ")
    print("========================================================= ")
    print()


# generate_receipt creates the receipt for the laptops sold by the administrator from the shop
def generate_receipt(laptop_item, laptop_quantity, recipient_name):
    """
    When invoked, all the details regarding the selling part is unpacked to generate a receipt on file as well as by printing on console

    Parameters:
        :param laptop_item: item id of laptop
        :param laptop_quantity: quantity of laptop
        :param recipient_name: name of the recipient

    Type:
        :type laptop_item: int
        :type laptop_quantity: int
        :type recipient_name: str

    """
    #
    now_ = datetime.now()
    # creating a file which does not pre-exist
    __ = open(f"./Receipts/{read.read()[laptop_item - 1][0]}_{recipient_name}_receipt_({now_.day}|{now_.month}|{now_.year})({now_.hour}:{now_.minute}:{now_.second}).txt", "x")

    # calculating shipping cost and total price
    shipping_cost = int(read.read()[laptop_item - 1][2]) * 0.03
    total_price = int(read.read()[laptop_item - 1][2]) * laptop_quantity

    # opening the file to write
    # receipt generated
    with open(f"./Receipts/{read.read()[laptop_item - 1][0]}_{recipient_name}_receipt_({now_.day}|{now_.month}|{now_.year})({now_.hour}:{now_.minute}:{now_.second}).txt", "w") as receipt:
        receipt.write("========================================================= \n")
        receipt.write(f"                 ByteBrew Technologies \n")
        receipt.write("========================================================= \n")
        receipt.write("SALE RECEIPT \n")
        receipt.write("\n")
        receipt.write("Putalisadak, Kathmandu 44600\n")
        receipt.write("P.O BOX: 3314-24500\n")
        receipt.write("TEL: 01-534029\n")
        receipt.write("EMAIL: laptop_shop@gmail.com\n")
        receipt.write("--------------------------------------------------------- \n")
        receipt.write(f" Sold to: {recipient_name} \n")
        receipt.write("--------------------------------------------------------- \n")
        receipt.write("| ITEM \t\t| NAME \t\t\t| QUANTITY \t|\n")
        receipt.write("--------------------------------------------------------- \n")
        # writing the details in a tabulated manner
        receipt.write(f"| {laptop_item})" + " " * (12 - len(str(laptop_item))) + " |" + f" {read.read()[laptop_item - 1][0]}" + " " * (
                21 - len(read.read()[laptop_item - 1][0])) + " |" + f" {laptop_quantity}" + " " * (
                              13 - len(str(laptop_quantity))) + " |" + "\n")
        receipt.write("--------------------------------------------------------- \n")
        receipt.write("\n")
        receipt.write(f" {str(now_)} \n")
        receipt.write("--------------------------------------------------------- \n")
        receipt.write(f"                                 Price: ${total_price} \n")
        receipt.write(f"                         Shipping cost: ${round(shipping_cost, 1)} \n")
        receipt.write(f"                           Total price: ${int(total_price) + shipping_cost} \n")
        receipt.write("--------------------------------------------------------- \n")
        receipt.write("                      x THANK YOU x \n")
        receipt.write("========================================================= \n")

    # printing the receipt on console
    print("========================================================= ")
    print(f"                 ByteBrew Technologies")
    print("========================================================= ")
    print("SALE RECEIPT ")
    print()
    print("Putalisadak, Kathmandu 44600")
    print("P.O BOX: 3314-24500")
    print("TEL: 01-534029")
    print("EMAIL: laptop_shop@gmail.com")
    print("========================================================= ")
    print(f"Sold to: {recipient_name}")
    print()
    print("--------------------------------------------------------- ")
    print("| ITEM \t\t| NAME \t\t\t| QUANTITY  \t|")
    print("--------------------------------------------------------- ")
    # printing the details in a tabulated manner
    print(f"| {laptop_item})", " " * (10 - len(str(laptop_item))), " |", f" {read.read()[laptop_item - 1][0]}", " " * (
            18 - len(read.read()[laptop_item - 1][0])), " |", f" {laptop_quantity}", " " * (
                                       10 - len(str(laptop_quantity))), " |")
    print("--------------------------------------------------------- ")
    print(f" {str(now_)} ")
    print("--------------------------------------------------------- ")
    print(f"                                 Price: ${total_price} ")
    print(f"                         Shipping cost: ${round(shipping_cost, 1)} ")
    print(f"                           Total price: ${int(total_price) + shipping_cost} ")
    print("--------------------------------------------------------- ")
    print("                    x THANK YOU x ")
    print("========================================================= ")
    print()
