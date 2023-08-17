import pandas as pd
import re

data = pd.read_excel("data-raw/fake-data.xlsx")

pattern = r'\b(\d{10}|\d{6}-\d{4})\b'

def cpr_validation(number):
    """
    Use this function to run CPR number validation process
    :param number: expecting to input 10 digit number
    :return: True to False
    """

    if len(str(number)) != 10:
        raise ValueError("Input must be a 10-digit number")

    constant = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

    multiplied_digits = [int(digit) * constant for digit, constant in zip(str(number), constant)]
    total = sum(multiplied_digits)

    if total % 11 == 0:
        return True
    return False

def extract_10_digit_numbers(text):
    pattern = r'\D(\d{10}|\d{6}-\d{4})\D'
    #pattern = r'\b\d{10}\b?|\d{10}|\d{6}-\d{4}'
    numbers = re.findall(pattern, str(text))
    return numbers

last_column_values = data.iloc[:, -1].to_list()
# data.transform()
# print(extract_10_digit_numbers(data.iloc[:, -1])[1])
print(list(map(extract_10_digit_numbers, last_column_values)))
#print(list(map(cpr_validation, extract_10_digit_numbers(data.iloc[:, -1].to_list))))
# print(data.iloc[:, -1].str.contains(pattern))
# print(data[data.iloc[:, -1].str.contains(pattern)])