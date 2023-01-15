import xml.etree.ElementTree as ET

tree = ET.parse("SWBF.CT")
root = tree.getroot()

entries_root = root.find("CheatEntries")

def loop(node, depth = 0, guideline_levels = []):
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

                loop(sub_cheat_entries, depth + 1, guideline_levels)

                # we ascend a level and want to remove the last guideline
                if len(guideline_levels) > 0:
                    guideline_levels.pop()


loop(entries_root)
