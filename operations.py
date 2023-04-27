# imports from other files as libraries
import read


# display method to display all the available laptops from the stock file
def display():
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
    if get_prompt == "exit":
        print("SYSTEM EXITING" + "." + "." + ".")
        print("EXITED")
        exit()
