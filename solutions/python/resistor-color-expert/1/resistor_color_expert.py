RESISTORS = {
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

TOLERANCE = {
    'grey' : '0.05%',
    'violet' : '0.1%',
    'blue' : '0.25%',
    'green' : '0.5%',
    'brown' : '1%',
    'red' : '2%',
    'gold' : '5%',
    'silver' : '10%',
}

def resistor_label(colors):
    if len(colors)== 1: return f"{RESISTORS[colors[0]]} ohms"
    ohms = (RESISTORS[colors[0]] * 100 + RESISTORS[colors[1]] * 10 + RESISTORS[colors[2]]) * 10 ** RESISTORS[colors[3]] if len(colors) > 4 else (RESISTORS[colors[0]] * 10 + RESISTORS[colors[1]]) * 10 ** RESISTORS[colors[2]]
    
    res_tolerance = TOLERANCE[colors[4]] if len(colors) > 4 else TOLERANCE[colors[3]] 
    if ohms >= 10 ** 9:
        prefix = "giga"
        ohms /= 10 ** 9
    elif ohms >= 10 ** 6:
        prefix = "mega"
        ohms /= 10 ** 6
    elif ohms >= 10 ** 3:
        prefix = "kilo"
        ohms /= 10 ** 3
    else:
        prefix = ""
    ohms = int(ohms) if ohms == int(ohms) else round(ohms, 2)
    return f"{ohms} {prefix}ohms ±{res_tolerance}"
