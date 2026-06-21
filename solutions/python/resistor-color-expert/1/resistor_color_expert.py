def resistor_label(colors):
    
    resistances = {
    "grey" : "±0.05%",
    "violet" : "±0.1%",
    "blue" : "±0.25%",
    "green" : "±0.5%",
    "brown" : "±1%",
    "red" : "±2%",
    "gold" : "±5%",
    "silver" : "±10%"
    }

    codes = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    prefixes = [ 
        "kilo", 
        "mega",
        "giga" 
    ] 

    
    output = ""

    if len(colors) == 1:
       return f"{codes.index(colors[0])} ohms"
        

    if len(colors) == 4: 
        color_1, color_2, color_3, color_4 = colors
        tolerance = resistances[color_4] 
        output += str(codes.index(color_1))
        output += str(codes.index(color_2))
        output = int(output) * (10 ** codes.index(color_3))



    if len(colors) == 5: 
        color_1, color_2, color_3, color_4, color_5 = colors
        tolerance = resistances[color_5]
        output += str(codes.index(color_1))
        output += str(codes.index(color_2))    
        output += str(codes.index(color_3))
        output = int(output) * (10 ** codes.index(color_4))



    if output // 10 ** 9 != 0:
        prefix = prefixes[2]
        output = output / 10 ** 9
    elif output // 10 ** 6 != 0:
        prefix = prefixes[1]
        output = output / 10 ** 6
    elif output // 10 ** 3 != 0:
        prefix = prefixes[0]
        output = output / 10 ** 3
    else:
        prefix = ""
        
    if isinstance(output, float) and output.is_integer():
        output = int(output)


    return f"{output} {prefix}ohms {tolerance}"   