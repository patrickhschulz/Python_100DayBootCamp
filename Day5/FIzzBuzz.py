for number in range(1, 101):
    if number % 3 == 0:
        print("Fizz")
    else:
        print(f"{number}")

    if number % 5 == 0:
        print("Buzz")
    else:
        print(f"{number}")

    if (number % 3 == 0) and (number % 5 ==0):
        print("FizzBuzz")
    else:
        print(f"{number}")