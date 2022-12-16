import os
import time

os.system("cls")


SCREEN_ITEMS = {
    "foreground-color": {
        "name": "Foreground Color",
        "items": {
            "white": "37",
            "black": "30",
            "red": "31",
            "green": "32",
            "blue": "34",
            "magenta": "35",
            "cyan": "36",
            "yellow": "33",
        },
        "selected": ""
    },
    "background-color": {
        "name": "Background Color",
        "items": {
            "white": "47",
            "black": "40",
            "red": "41",
            "green": "42",
            "blue": "44",
            "magenta": "45",
            "cyan": "46",
            "yellow": "43",
        },
        "selected": ""
    },
    "text-stlye": {
        "name": "Text Style",
        "items": {
            "bold": "1",
            "italic": "3",
            "underline": "4",
            "strikethrough": "9",
        },
        "selected": ""
    }
}


# Formats any text with the given ANSI escape codes and returns it
def make_escaped_text(codes: list[str], text: str):
    formatted_text = "\033[" + ";".join(codes) + "m" + text + "\033[0m"
    return formatted_text


# Returns a printable (to the terminal) ANSI escape code sequence
def make_printable_escape_code(codes: list[str]):
    # note the second backslash
    code = "\\033[" + ";".join(codes) + "m"
    return code


# Formats the selected ANSI escape codes into a string to be displayed to the user
def get_final_code():
    codes = []
    for key in SCREEN_ITEMS:
        item_name = SCREEN_ITEMS[key]["selected"]
        if not item_name:
            continue
        codes.append(SCREEN_ITEMS[key]["items"][item_name])

    if not len(codes): 
        return "Maybe make a selection first ¯\\_(ツ)_/¯"

    return make_printable_escape_code(codes) + make_escaped_text(codes, "TEXT HERE") + make_printable_escape_code(["0"])


# Prints the selected options nicely formatted next to the main menu entries
def print_selection(current_screen):
    selection = SCREEN_ITEMS[current_screen]["selected"]
    if selection:
        print(":", make_escaped_text([SCREEN_ITEMS[current_screen]["items"][selection]], selection))
    else:
        print() # we need a linebreak if we got no selection


# Handle all the screen rendering stuff
def push_screen(screen_key = ""):
    # This is used to cleanup before we display a new screen
    # move cursor to home -> 
    # move cursor few lines down to keep header -> 
    # delete everything until end of screen
    print("\033[H" "\033[3E" "\033[0J", end="")

    # home screen
    if not screen_key or screen_key == "home":
        print("│", "\033[1mMAIN MENU\033[0m", "\n│")
        for index, keys in enumerate(SCREEN_ITEMS.keys()):
            print(f"┝ {index + 1})", SCREEN_ITEMS[keys]["name"], end="")
            print_selection(keys)
            time.sleep(0.1)


        print("│\n┝", "0) Get Code")
        print("└────────────────────────────")
        handle_navigation("home")

    # all other screens
    else:
        print("│\033[1m", SCREEN_ITEMS[screen_key]["name"], "\033[0m\n│")
        for index, (name, code) in enumerate(SCREEN_ITEMS[screen_key]["items"].items()):
            print(f"┝ {index + 1})", make_escaped_text([code], "▆"), name)
            time.sleep(0.05)

        print("│\n┝", "0) Back")
        print("└────────────────────────────")
        handle_navigation(screen_key)


# Handling user input for all screens 
def handle_navigation(current_screen):
    while True:
        try:
            # choice will be used to select the desired option
            # we're going to do choice-1 further down to go zero-indexed
            choice = int(input("> "))

            if current_screen == "home":
                if choice == 0:
                    print("\n", get_final_code(), "\n")
                    continue

                # check if choice is valid
                keys = list(SCREEN_ITEMS.keys())
                if not choice - 1 in range(len(keys)):
                    raise ValueError
                push_screen(keys[choice - 1]) # go to chosen screen

            else: # all other screens
                if choice == 0:
                    push_screen() # go to home screen
                
                # check if choice is valid
                keys = list(SCREEN_ITEMS[current_screen]["items"].keys())
                if not choice - 1 in range(len(keys)):
                    raise ValueError
                
                # user selected something
                print(SCREEN_ITEMS[current_screen]["name"] + ":", keys[choice - 1], "selected")
                # store what the user has selected
                SCREEN_ITEMS[current_screen]["selected"] = keys[choice - 1]
                time.sleep(1)
                push_screen() # go to home screen

        except ValueError:
            print("Please choose a valid option")
            continue


# header
print("┌────────────────────────────┐")
print("│ \033[33;1mANSI Escape Code Generator\033[0m │")
print("├────────────────────────────┘")
time.sleep(0.1)

# home screen
push_screen()
