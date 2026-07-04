def line_up(name, number):

    num = str(number)

    if num[-1] == "1" and num[-2:-1] != "1":
        ending = "st"
    elif num[-1] == "2" and num[-2:-1] != "1":
        ending = "nd"
    elif num[-1] == "3" and num[-2:-1] != "1":
        ending = "rd"
    else:
        ending = "th"


    return f"{name}, you are the {number}{ending} customer we serve today. Thank you!"
