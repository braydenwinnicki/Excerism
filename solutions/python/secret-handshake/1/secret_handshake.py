def commands(binary_str):

    active_str = binary_str[-5:].zfill(5)
   

    actions = {
    "00001" : "wink",
    "00010" : "double blink",
    "00100" : "close your eyes",
    "01000" : "jump"
    }

    new_str = []

    if active_str[4] == "1":
        new_str.append(actions["00001"])
    if active_str[3] == "1": 
        new_str.append(actions["00010"])
    if active_str[2] == "1": 
        new_str.append(actions["00100"])
    if active_str[1] == '1': 
        new_str.append(actions['01000'])
    if active_str[0] == '1': 
        new_str = new_str[::-1]

    return new_str
    