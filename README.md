# CPR Number Check

This script extracts and validates 10-digit CPR numbers from an Excel sheet's specified column.

## Requirements

- Python 3.x
- pandas library (can be installed using `pip install pandas`)

## Usage

1. Clone or download this repository to your local machine.
2. Navigate to the repository's directory using your terminal/command prompt.

## Running the Script

Move the target Excel sheet into same directory.

The script can be run using the following command:

```bash
python check_cpr_number.py excel_file_name target_column_name
```

To use the default column name as "Linjeindhold for 1. fund"

```bash
python check_cpr_number.py excel_file_name
```

## Example Output
```bash
[
    {
        "row_number": 1,
        "numbers": [
            {"number": "1234567890", "label": "CPR Valid"},
            {"number": "9876543210", "label": "invalid"}
        ]
    },
    {
        "row_number": 2,
        "numbers": "No 10 digit number found"
    },
    ...
]
```