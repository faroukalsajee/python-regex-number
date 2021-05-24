import re, os  # importing re and os libraries


def validate_book_order_details(order_num, title, author, isbn, year, quantity, cost):
    """In this function we will validate order_num title author isbn number year quantity and cost using regex"""
    check_order_num = re.match('\d+(?![\w\. ])', str(
        order_num))  # checking if the number are digits and doesn't contain . space or letters
    if not check_order_num:  # It's matching true if valid so we put "not" to check for invalid input
        raise ValueError("Order Number is invalid")

    global order_num_  # making order number global variable to use it in another function
    order_num_ = order_num  # assigning the parameter order_num to order_num_ variable

    check_title = re.match('[A-Za-z ]+', title)  # checking if the title contains upper and lower letter and spaces
    if not check_title:
        raise ValueError("Title is invalid")
    check_author = re.match('(?![\d_-])', author)  # checking that author name doesn't contain digits _ or -
    if not check_author:
        raise ValueError("Author is invalid")
    check_isbn = re.match('\d+(?![\.\w _] )', isbn)  # checking that isbn is digits and not letters or .
    if not check_isbn:
        raise TypeError("ISBN must be an integer")
    check_isbn1 = re.match('^\d{4,20}$', isbn)  # checking that number of digits in isbn is between 4 and 20 inclusive
    if not check_isbn1:
        raise ValueError("ISBN is invalid")
    check_year = re.match('\d+(?![\.\w] )', str(year))  # checking that year is digits and not letters
    if not check_year:
        raise TypeError("Year must be an integer")
    check_year1 = re.match('^[0-9]{4}$', str(year))  # making sure that year was 4 digits only
    if not check_year1:
        raise ValueError("Year is invalid")
    check_quantity = re.match('\d+(?![\.\w])', quantity)  # checking that isbn is digits and not letters or float.
    if not check_quantity:
        raise TypeError("Quantity must be an integer")
    check_quantity1 = float(quantity) >= 0 and float(
        quantity) <= 1000  # checking that quantity is between 0 and 1000 inclusive
    if not check_quantity1:
        raise ValueError("Quantity is invalid")
    check_cost = "{0:.2f}".format(float(cost)) == str(cost)  # checking that cost is 2 decimal round float number
    if not check_cost:
        raise ValueError("Cost is invalid")
    return True


def calculate_per_book_cost(cost, quantity):
    """Calculating the unit_cost"""
    try:
        return float(cost) / int(quantity)
    except ZeroDivisionError:  # expecting the zero division
        raise ZeroDivisionError("No Books in Order")  # raise error message that we want


def write_book_order_details(filename, title, author, isbn, year, quantity, cost, unit_cost):
    """Writing Book Order in txt file"""
    if os.path.exists(
            filename):  # not case sensitive but we are working on windows so it doen't matter windows file system is
        # case insensitive is open("test.txt") is the same as open("TEST.txt")
        raise ValueError("Order file name already exists!")
    lines = ["BOOK ORDER {}\n".format(order_num_), "title={}\n".format(title), "author={}\n".format(author),
             "isbn={}\n".format(isbn), "year={}\n".format(year), "quantity={}\n".format(quantity),
             "cost=${}\n".format(cost),
             "unit_cost=${}".format(unit_cost)]  # making lines of the file in one list to use it in writelines function
    with open(filename, 'w+') as f:  # using with to open file to close it automatically
        f.writelines(lines)  # writing lines
