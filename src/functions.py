from random import randint

def even_odd(number):
    if isinstance(number, int):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Please use an integer value"


def get_largest(x, y, z):
    # use the x value as largest value
    largest = x

    # if y is large: replace the largest value by y
    if largest < y:
        largest = y

    # if z is large: replace the largest value by z
    if largest < z:
        largest = z

    # return the largest value
    return largest


def dice_rolling():
    face = randint(1,6)
    return face