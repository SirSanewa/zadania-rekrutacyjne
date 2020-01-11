"""
ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.
"""

import numpy
import decimal


def numbers_generator():
    decimal_list = []
    for floaty in numpy.arange(2.0, 5.5, 0.5):
        decimal_list.append(decimal.Decimal(floaty).quantize(decimal.Decimal(".01")))
    return decimal_list


if __name__ == "__main__":
    print(numbers_generator())