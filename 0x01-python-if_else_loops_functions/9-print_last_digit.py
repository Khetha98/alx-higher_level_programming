def print_last_digit(number):
    if number < 0:
        digit = number % -10
        print(-1*digit, end="")
    else:
        digit = number % 10
        print(digit, end="")
    return abs(digit)