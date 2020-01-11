"""
ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]
"""


def list_creator(numbers_range):
    list = []
    while len(list) != numbers_range:
        for number in range(numbers_range):
            list.append(number + 1)
    return list


def missing_numbers(numbers_range, numbers):
    numbers_list = list_creator(numbers_range)
    for number in numbers:
        if number in numbers_list:
            numbers_list.remove(number)
    return numbers_list


if __name__ == "__main__":
    number_range = 10
    numbers = [2, 3, 7, 4, 9]
    print(missing_numbers(number_range, numbers))
