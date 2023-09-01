from datetime import datetime


class Validation:
    def validate_date(number):
        # Implement the date validation logic here (DDMMYY format)
        # Return True if number is in the correct format otherwise False
        number_str = str(number)

        if len(number_str) != 6:
            raise ValueError("Input must be a 6-digit number")

        try:
            # Parse the number as a date in the format DDMMYY
            date_obj = datetime.strptime(number_str, '%d%m%y')
        except ValueError:
            return False

        return True

    def cpr_validation(number):
        """
        Use this function to run CPR number validation process
        :param number: expecting to input 10 digit number
        :return: True to False
        """

        if len(str(number)) != 10:
            raise ValueError("Input must be a 10-digit number")

        constant = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

        multiplied_digits = [int(digit) * constant for digit, constant in
                             zip(str(number), constant)]
        total = sum(multiplied_digits)

        if total % 11 == 0:
            return True
        return False
