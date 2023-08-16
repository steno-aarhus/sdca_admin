import pandas as pd
import re


class ExcelNumberExtractor:
    DEFAULT_COLUMN_NAME = "Linjeindhold for 1. fund"

    def __init__(self, excel_file, last_column_name=DEFAULT_COLUMN_NAME):
        self.excel_file = excel_file
        self.last_column_name = last_column_name
        self.df = self.read_excel()

    def read_excel(self):
        return pd.read_excel(self.excel_file)

    def extract_numbers_with_rows(self):
        last_column = self.df[self.last_column_name]
        numbers_with_rows = {}

        for row_num, cell_value in enumerate(last_column, start=1):
            numbers = self.extract_10_digit_numbers(cell_value)
            if numbers:
                numbers_with_rows[row_num] = numbers

        return numbers_with_rows

    def extract_10_digit_numbers(self, text):
        pattern = r'\b\d{10}\b|\d{10}'
        numbers = re.findall(pattern, str(text))
        return numbers

    def get_dataframe(self):
        return self.df
