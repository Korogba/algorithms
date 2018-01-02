# implementation by @kaba_y, https://korogba.github.io


def karatsuba(x, y, base) -> float:
    """
    Multiply two n-digit number using the Karatsuba algorithm: https://brilliant.org/wiki/karatsuba-algorithm/
    :param x: multiplicand
    :param y: multiplier
    :param base: base that numbers are in: currently only decimal (base-10) values supported
    :return: product of (x * y) solved using the Karatsuba algorithm: https://en.wikipedia.org/wiki/Karatsuba_algorithm
    """
    # Ensure integer values are passed
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Invalid parameters supplied: Expects integer values")

    if x < base or y < base:
        return x * y

    x_string = str(x)
    y_string = str(y)

    max_size = max(len(x_string), len(y_string))
    half_length = max_size // 2

    x_left = x_string[:-half_length]
    x_right = x_string[-half_length:]

    y_left = y_string[:-half_length]
    y_right = y_string[-half_length:]

    p_one = karatsuba(int(x_left), int(y_left), base)
    p_three = karatsuba((int(x_left) + int(x_right)), (int(y_left) + int(y_right)), base)
    p_two = karatsuba(int(x_right), int(y_right), base)

    return (p_one * base ** (2 * half_length)) + ((p_three - p_one - p_two) * base ** half_length) + p_two
