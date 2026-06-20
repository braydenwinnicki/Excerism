def label(colors):
    codes = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue", 
        "violet",
        "grey", 
        "white", 
    ]

    prefixes = [ 
        "kilo", 
        "mega",
        "giga" 
    ] 

    output = ""

    color_1, color_2, color_3, *rest = colors

    output += str(codes.index(color_1))
    output+= str(codes.index(color_2))

    output = int(output) * 10 ** codes.index(color_3)

    if output // 10 ** 9 != 0:
        prefix = prefixes[2]
        output = output // 10 ** 9
    elif output // 10 ** 6 != 0:
        prefix = prefixes[1]
        output = output // 10 ** 6
    elif output // 10 ** 3 != 0:
        prefix = prefixes[0]
        output = output // 10 ** 3
    else:
        prefix = ""


    return f"{output} {prefix}ohms"   