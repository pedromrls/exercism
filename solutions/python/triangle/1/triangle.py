def equilateral(sides):
    if (not sides or 0 in sides): return False
    a,b,c = sides
    return a == b == c and (a + b >= c and a + c >= b and b + c >= a)


def isosceles(sides):
    if (not sides or 0 in sides): return False
    a,b,c = sides
    return (a == b or b == c or a == c) and (a + b >= c and a + c >= b and b + c >= a)

def scalene(sides):
    if (not sides or 0 in sides ): return False
    a,b,c = sides
    return (a != b and b != c and a != c) and (a + b >= c and a + c >= b and b + c >= a)
