import sys
import json
from extractor import ExcelNumberExtractor
from validation import Validation
from generate_output import generate_excel_sheets


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_cpr_number.py <excel_file> [last_column]")
        sys.exit(1)

    excel_file = sys.argv[1]

    if len(sys.argv) == 3:
        last_column_name = sys.argv[2]
    else:
        last_column_name = ExcelNumberExtractor.DEFAULT_COLUMN_NAME

    extractor = ExcelNumberExtractor(excel_file, last_column_name)
    numbers_with_rows = extractor.extract_numbers_with_rows()
    row_count = len(numbers_with_rows)

    # Get the total number of rows from the Excel sheet
    total_row_count = extractor.get_dataframe().shape[0]

    print(f"Total rows in Excel sheet: {total_row_count}")
    print(f"Rows with 10-digit numbers: {row_count}")
    print("Running CPR Number Validation Process...")
    cpr_validation_result = []

    for row_num in range(1, total_row_count + 1):
        if row_num in numbers_with_rows:
            numbers = numbers_with_rows[row_num]
            validated_numbers = []

            for number in numbers:
                if Validation.validate_date(number[:6]) and \
                        Validation.cpr_validation(number):
                    validated_numbers.append(
                        {"number": number, "label": "CPR Valid"})
                else:
                    validated_numbers.append(
                        {"number": number, "label": "invalid"})
            row_data = {
                "row_number": row_num,
                "numbers":
                    validated_numbers if validated_numbers else "No 10 digit"
            }
        else:
            row_data = {
                "row_number": row_num,
                "numbers": [
                    {
                        "number": "None",
                        "label": "No 10 digit"
                    }
                ]
            }
        cpr_validation_result.append(row_data)

    # Print the JSON data for testing only and
    # will be removed for the fincal version
    # print(json.dumps(cpr_validation_result, indent=4))
    generate_excel_sheets(cpr_validation_result, excel_file, total_row_count)


if __name__ == "__main__":
    main()
