RES_COLOR = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

def label(colors):
    color_1, color_2, color_3 = RES_COLOR[colors[0]], RES_COLOR[colors[1]], RES_COLOR[colors[2]]
    ohms = (color_1 * 10 + color_2) * 10 ** color_3
    prefix = "ohms"
    
    if ohms > (10 ** 9):
        prefix = "gigaohms" 
        ohms //= 10 ** 9
    elif ohms > (10 ** 6):
        prefix = "megaohms"
        ohms //= 10 ** 6
    elif ohms > (10 ** 3): 
        prefix = "kiloohms"
        ohms //= 10 ** 3
    
    
    return f"{ohms} {prefix}"
