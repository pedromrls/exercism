def is_armstrong_number(number):
    digits = str(number)
    number_of_digits = len(digits)
    sum = 0
    for digit in digits:
        sum += int(digit) ** number_of_digits
    
    return sum == number