def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b): raise ValueError("Strands must be of equal length.")
    return sum(1 for ind in range(len(strand_a)) if strand_a[ind] != strand_b[ind])
