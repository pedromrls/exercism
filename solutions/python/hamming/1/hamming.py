def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b): raise ValueError("Strands must be of equal length.")

    diff = 0
    for ind, char in enumerate(strand_a):
        if char != strand_b[ind]: diff += 1

    return diff
