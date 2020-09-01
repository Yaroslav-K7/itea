
""""first task"""
b = []


def list_numbers(number):
    for i in range(number):
        if i % 2 == 0:
            b.append(i)
    return b


input_numbers = input("Your input: ")
list_numbers(int(input_numbers))

"""second task"""
library_countries = {
    "Ukraine": "Kyiv",
    "Russia": "Moscow",
    "Belarus": "Minsk",
    "Franse": "Paris",
    "Italy": "Rome"
}
countries = ["Ukraine", "Russia", "Belarus", "France", "Italy"]

for countr in countries:
    if countr in library_countries:
        print(library_countries[countr])

"""third task"""
for j in range(1, 101):
    if j % 3 != 0 and j % 5 != 0 and j % 15 != 0:
        print(i)
    if j % 3 == 0 and j % 15 != 0:
        print("Fizz")
    if j % 5 == 0 and j % 15 != 0:
        print("Buzz")
    if j % 15 == 0:
        print("FizzBuzz")


"""fourth task"""


def bank(sum_dep, years, percent):
    for m in range(1, years + 1):
        sum_dep += sum_dep * percent * 0.01
    return round(sum_dep, 2)
