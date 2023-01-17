import xml.etree.ElementTree as ET
import sys


# allow output redirect (>) into files on windows
sys.stdout.reconfigure(encoding="utf-8")


def dump(node, depth = 0, guideline_levels = []):
    for index, elem in enumerate(node):
        if elem.tag == "CheatEntry":
            caption           = elem.find("Description").text.replace('"', "")
            sub_cheat_entries = elem.find("CheatEntries")
            num_of_childs     = len(node)
            is_last_child     = index + 1 == num_of_childs
            

            if depth > 1:
                for i in range(depth - 1):
                    try:
                        if guideline_levels[i] == 1:
                            print("│", end="")
                        else:
                            print(" ", end="")
                    except IndexError:
                        print(" ", end="")

                    print(" " * 3, end="") # generic padding for each level of depth


            if depth > 0:
                if is_last_child:
                    print("└─ ", end="")
                else:
                    print("├─ ", end="")


            print(caption)


            if sub_cheat_entries:
                # if we're last child we dont want to keep printing the *current* guideline on the next lines
                if is_last_child:
                    if len(guideline_levels) > 0:
                        guideline_levels.pop()
                        guideline_levels.append(0)
                
                # Rule of thumb: length of guideline_levels is equal to depth
                # we decend one level deeper =  new guideline
                guideline_levels.append(1)

                dump(sub_cheat_entries, depth + 1, guideline_levels)

                # we ascend a level and want to remove the last guideline
                if len(guideline_levels) > 0:
                    guideline_levels.pop()


def main():
    try:
        filepath = sys.argv[1]

        tree = ET.parse(filepath)
        root = tree.getroot()

        entries_root = root.find("CheatEntries")

        dump(entries_root)

    except IndexError:
        print("Error: Please specify the path to a file as the first argument.")

    except ET.ParseError:
        print(f"Error: The file '{filepath}' could not be parsed.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' could not be found.")

    except IsADirectoryError:
        print(f"Error: '{filepath}' is a directory.")

    except OSError:
        print(f"Error: '{filepath}' is not a valid argument. Wildcards are not supported.")

main()
