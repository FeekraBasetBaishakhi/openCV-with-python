def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit} hour"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit} minute"
    else:
        return "Unsupported Unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_num = int(days_and_unit_dictionary["days"])
        # we only need conversion for positive integer value
        if user_input_num > 0:
            cal_value = days_to_units(user_input_num, days_and_unit_dictionary["unit"])
            print(cal_value)
        elif user_input_num == 0:
            print("Days for 0 have no result")
        else:
            print("Value Cannot be Negative")

    except ValueError:
        print("Input you just given, it is not integer.\nTry Again")


user_input_message = "Ola! amigo, enter number of days and conversion unit!\n"
