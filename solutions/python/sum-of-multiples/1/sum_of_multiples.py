def sum_of_multiples(limit, multiples):
    multiple = set()
    for mul in multiples:
        if mul != 0:
            for num in range(1, limit):
                if num % mul == 0:
                    multiple.add(num)

    return sum(multiple)
    
    
