"""
ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi
"""


def zip_to_int(zip_code):
    parts = zip_code.split('-')
    value = ''.join(parts)
    return int(value)


def zip_codes_generator(start, stop, step=1):
    start = zip_to_int(start)
    stop = zip_to_int(stop) + 1
    for zip_code in range(start, stop, step):
        begin = str(zip_code)[:2]
        end = str(zip_code)[2:5]
        print('{:02}-{:03}'.format(int(begin), int(end)))


if __name__ == "__main__":
    zip_codes_generator("79-900", "80-155")
