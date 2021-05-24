import sys
import lab_10

if __name__ == "__main__":
    if len(sys.argv) != 9:  # main.py is considered as an argument and the other 8 argument then the total is 8 + 1 = 9
        print("Wrong Input , terminating the program ... ")
        sys.exit()  # terminating the program

    filename = sys.argv[1]
    order_num = sys.argv[2]
    title = sys.argv[3]
    author = sys.argv[4]
    isbn = sys.argv[5]
    year = sys.argv[6]
    quantity = sys.argv[7]
    cost = sys.argv[8]

    lab_10.validate_book_order_details(order_num, title, author, isbn, year, quantity,
                                       cost)  # validating the input
    unit_cost = lab_10.calculate_per_book_cost(cost, quantity)  # calculating the unit cost
    lab_10.write_book_order_details(filename, title, author, isbn, year, quantity, cost,
                                    unit_cost)  # writing the txt file
