RESIS_COLOR = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
}
def value(colors):
    return RESIS_COLOR[colors[0]] * 10 + RESIS_COLOR[colors[1]]
