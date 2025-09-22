def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum = sum(factor for factor in range(1, number//2 + 1) if number % factor == 0)
    if aliquot_sum == number: return "perfect"        
    elif aliquot_sum > number: return "abundant"
    else: return "deficient"