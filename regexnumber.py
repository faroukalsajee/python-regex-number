import re


# implementing regex to find number in range 32- 126
def check_range(number):
    regex = "^(3[2-9]|[4-9][0-9]|1[0-1][0-9]|12[0-6])$"
    if re.search(regex, str(number)):
        print("Number is in range 32- 126")
    else:
        print("Number isn't in range 32- 126")
