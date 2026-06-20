def value(colors):

    options = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
    ]
    
    color_1, color_2, *rest = colors 

    str_version = str(options.index(color_1)) + str(options.index(color_2))

    return int(str_version)

    
