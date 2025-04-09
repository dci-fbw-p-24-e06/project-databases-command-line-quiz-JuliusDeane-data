import bcrypt
import base64


def check_int_input(text, int_range=(1, 999999), exclude=[]):
    choice = ""
    while not choice:
        try:
            choice = int(input(text))
        except ValueError:
            print("Wrong input. Please only input a number.")
            choice = ""
        if (choice not in range(*int_range) or choice in exclude) and isinstance(
            choice, int
        ):  # noqa
            print("Number out of range. Please choose a valid number.")
            choice = ""
    else:
        return choice


def check_str_input_whitelist(
    text: str, whitelist: list, show_list: str = "n"
) -> str:
    choice = ""
    while not choice:
        choice = input(text)
        if choice not in whitelist and show_list == "y":
            print(f"Wrong input. Allowed input: {", ".join(whitelist)}.")
            choice = ""
        elif choice not in whitelist and show_list == "n":
            print(f"Wrong input. '{choice}' not allowed. Please try again.")
            choice = ""
    else:
        return choice


def check_str_input_blacklist(
    text: str, blacklist: list, show_list: str = "n"
) -> str:
    choice = ""
    while not choice:
        choice = input(text)
        if choice in blacklist and show_list == "y":
            print(f"Wrong input. Do not use: {", ".join(blacklist)}.")
            choice = ""
        elif choice in blacklist and show_list == "n":
            print(f"Wrong input. '{choice}' not allowed. Please try again.")
            choice = ""
    else:
        return choice


def set_password():
    password = ""
    while not password:
        password = input("Insert password: ")
        if not 6 <= len(password) <= 25:
            print("Not allowed. Password must be between 6 and 25 characters.")
            password = ""
        else:
            check_str_input_whitelist("Repeat password: ", [password])
            hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            hashed_pw_base64 = base64.b64encode(hashed_pw).decode("utf-8")
            return hashed_pw_base64


def check_password(base64_password):
    player_password = base64.b64decode(base64_password)
    success = False
    n = 3
    while not success and n > 0:
        pw_input = input("Insert password: ")
        success = bcrypt.checkpw(pw_input.encode(), player_password)
        if not success:
            n -= 1
            print(f"Wrong password. {n}/3 attempts left.")
    return success


if __name__ == "__main__":
    print(
        set_password()
    )
