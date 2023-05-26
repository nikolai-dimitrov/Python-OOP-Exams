def name_validator(value, message):
    if value == "" or value.isspace():
        raise ValueError(message)


def number_validator(value, message):
    if value <= 0:
        raise ValueError(message)
