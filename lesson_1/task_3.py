for j in range(1, 101):
    if j % 15 == 0:
        print("FizzBuzz")
    elif j % 5 == 0:
        print("Buzz")
    elif j % 3 == 0:
        print("Fizz")
    else:
        print(j)
