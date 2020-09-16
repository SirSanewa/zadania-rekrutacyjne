"""
ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]
"""

def missing_numbers_list(entry_list, end_number):
    return [number for number in range(1, end_number+1) if number not in entry_list]


if __name__ == "__main__":
    number_range = 10
    numbers = [2, 3, 7, 4, 9]
    print(missing_numbers_list(numbers, number_range))
