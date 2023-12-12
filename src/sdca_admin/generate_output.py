import pandas as pd

CPR_VALID_FILE = "CPR_likely_output.xlsx"
CPR_INVALID_FILE = "CPR_unlikely_output.xlsx"


def generate_excel_sheets(
        cpr_validation_result,
        excel_file,
        total_row_count,
        valid_output_file=CPR_VALID_FILE,
        invalid_output_file=CPR_INVALID_FILE
):

    df = pd.read_excel(excel_file)
    valid_rows = []

    total_row_list = list(range(1, total_row_count + 1))
    for row_data in cpr_validation_result:
        row_number = row_data["row_number"]
        for number_info in row_data["numbers"]:
            if number_info["label"] == "CPR Valid":
                valid_rows.append(row_number)
                continue

    print(f"Found {len(valid_rows)} rows contains valid CPR numbers.")
    # create the invalid CPR rows number list
    invalid_rows = [item for item in total_row_list if item not in valid_rows]

    # Convert the row number into 0 base dataframe index
    valid_cpr_index = [index - 1 for index in valid_rows]
    invalid_cpr_index = [index - 1 for index in invalid_rows]

    # Create the sub dataframe for the valid and invalid dataframe
    valid_df = df.iloc[valid_cpr_index]
    invalid_df = df.iloc[invalid_cpr_index]

    # Output to Excel sheet
    print("Generating Output...")
    valid_df.to_excel(valid_output_file, index=False)
    print(f"Create {valid_output_file} excel sheet.")
    invalid_df.to_excel(invalid_output_file, index=False)
    print(f"Create {invalid_output_file} excel sheet.")
