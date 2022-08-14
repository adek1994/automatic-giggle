def fizzbuzz(number: int) -> str:
    if number % 15 == 0:
        return "Fizzbuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 ==0:
        return "Buzz"
    else:
        return number


if __name__ == "__main__":
    print(fizzbuzz(33))

