def check_int_input(text, int_range=(1, 999999), exclude=[]):
    choice = ""
    while not choice:
        try:
            choice = int(input(text))
        except ValueError:
            print("Wrong input. Please only input a number.")
            choice = ""
        if (choice not in range(*int_range) or choice in exclude) and isinstance(choice, int):
            print("Number out of range. Please choose a valid number.")
            choice = ""
    else:
        return choice


def check_str_input_whitelist(text: str, whitelist: list) -> str:
    choice = ""
    while not choice:   
        choice = input(text) 
        if choice not in whitelist:
            print(f"Wrong input. Allowed input: {", ".join(whitelist)}.")
            choice = ""
    else:
        return choice


def check_str_input_blacklist(text: str, blacklist: list, show_list: str = 'n') -> str:
    choice = ""
    while not choice:   
        choice = input(text) 
        if choice in blacklist and show_list == 'y':
            print(f"Wrong input. Do not use: {", ".join(blacklist)}.")
            choice = ""
        elif choice in blacklist and show_list == 'n':
            print(f"Wrong input. '{choice}' not allowed. Please try again.")
            choice = ""
    else:
        return choice

if __name__ == '__main__':
    print(check_str_input_blacklist("Guess valid number: ", ['12', '13', 'abc', 'dwg'], show_list='y'))