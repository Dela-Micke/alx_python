import random
def last_digit(num):
    last_digit_unsigned = abs(num) % 10
    return last_digit_unsigned if (num < 0) else last_digit_unsigned

number = random.randint(-10000,10000)
#print("Last digit of ",last_digit(number),"is",last_digit(number))
if last_digit(number) > 5:
    print("Last digit of ",number,"is",last_digit(number),"and is greater than 5\n")
elif last_digit(number) == 0:
    print("Last digit of ",number,"is",last_digit(number),"and is 0\n")
elif last_digit(number) < 6 and last_digit(number) != 0:
    print("Last digit of ",number,"is",last_digit(number),"and is less than 6 and not 0\n")