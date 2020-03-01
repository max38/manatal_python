def int_to_roman(int_value):
    if not isinstance(int_value, int):
        raise TypeError("expected integer, got {}".format(type(int_value)))
    if not 0 < int_value < 4000:
        raise ValueError("Argument must be between 1 and 3999")

    roman_mapper = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }

    result = []

    for roman_value in roman_mapper:
        count_letter = int(int_value / roman_value)
        result.append(roman_mapper[roman_value] * count_letter)
        int_value -= roman_value * count_letter

    return ''.join(result)


if __name__== "__main__":
    print(int_to_roman(500))
    print(int_to_roman(490))
    print(int_to_roman(3579))
