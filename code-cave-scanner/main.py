import sys
import os


def find_code_caves(filename, min_size):
    try:
        with open(filename, "rb") as file:
            # read the entire file into a byte array
            file_data = file.read()

        # cache
        file_data_length = len(file_data)

        # a list of dicts that store the size and addr of the code caves
        code_caves = []

        # searching for code caves
        i = 0
        while i < file_data_length:
            print(f"Scanning file: {int(100 / file_data_length * i)} %  |  {len(code_caves)} code caves found", end="\r")

            if file_data[i] != 0x0:
                i += 1
                continue
            
            size = 0

            # loop over the following bytes finding end of code cave
            j = i
            while j < file_data_length and file_data[j] == 0x0:
                size += 1
                j += 1
            
            # if the code cave is large enough, add it to the list
            if size >= int(min_size):
                code_caves.append((hex(i), size))

            # skip to end of code cave since we already scanned the bytes
            i = j
    except KeyboardInterrupt:
        ...

    return code_caves


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename> [min_size = 100]")
        sys.exit(1)
    
    filename = sys.argv[1]
    min_size = sys.argv[2] if len(sys.argv) > 2 else 100

    code_caves = find_code_caves(filename, min_size)

    code_caves.sort(key=lambda x: x[1], reverse=True)

    os.system("cls" if os.name == "nt" else "clear")
    
    if len(code_caves) < 1:
        print(f"Found no code caves with the desired size of {min_size} bytes. :<\033")
    else:
        print("Address".ljust(12), "Size")
        print("-" * 20)
        for cave in code_caves:
            print(str(cave[0]).ljust(12), f"{cave[1]}")
        print(f"\nFound {len(code_caves)} code caves with a minimum size of {min_size} bytes.")


main()
