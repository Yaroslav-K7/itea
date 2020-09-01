b = []


def list_numbers(number):
    for i in range(number):
        if i % 2 == 0:
            b.append(i)
    return b


input_numbers = input("Your input: ")
list_numbers(int(input_numbers))
