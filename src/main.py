import os
import time

os.system("cls")

RESET = "\033[0m"

SCREEN_ITEMS = {
    "foreground-color": {
        "name": "Foreground Color",
        "items": {
            "white": "\033[37m",
            "black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "blue": "\033[34m",
        },
    },
    "background-color": {
        "name": "Background Color",
        "items": {
            "white": "\033[37m",
            "black": "\033[30m"
        },
    },
    "text-stlye": {
        "name": "Text Style",
        "items": {
            "white": "\033[37m",
            "black": "\033[30m"
        },
    }
}

def display_screen(key = ""):
    # home screen
    if not key: 
        for index, keys in enumerate(list(SCREEN_ITEMS.keys())):
            print(f"┝ {index + 1})", SCREEN_ITEMS[keys]["name"])
            time.sleep(0.1)
    # all other screens
    else:
        print("│", SCREEN_ITEMS[key]["name"], "\n│")
        for index, item in enumerate(list(SCREEN_ITEMS[key]["items"].items())):
            print(f"┝ {index + 1})", item[1] + "▆" + "\033[0m", item[0])
            time.sleep(0.1)
    
    print("└────────────────────────────┘")


# header
print("┌" + "─" * 28 + "┐")
print("│ \033[35mANSI Escape Code Generator\033[0m │")
print("┝━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥")
time.sleep(0.1)

# home screen
display_screen()

choice = int(input("> "))

if choice: display_screen(list(SCREEN_ITEMS.keys())[choice - 1])
