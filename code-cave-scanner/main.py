import sys
import os


def find_code_caves(filename, min_size):
    try:
        with open(filename, "rb") as file:
            # read the entire file into a byte array
            file_data = file.read()

        # cache
        file_data_length = len(file_data)

        # a list of tuples that store the addr and size of the code caves
        code_caves = []

        # searching for code caves
        i = 0
        while i < file_data_length:
            print(f"Scanning file: {int(100 / file_data_length * i)} %  |  {len(code_caves)} code caves found", end="\r")

            # we're only interested in 0x00 code caves
            if file_data[i] != 0x0:
                i += 1
                continue
            
            size = 0

            # loop over the following bytes finding the end of the code cave
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
        # This try-except block allows the keyboard interrupt to prematurely exit the scan 
        # and display the code caves found up to that point.
        ...

    return code_caves


def main():
    try:
        filename = sys.argv[1]

        min_size = int(sys.argv[2] if len(sys.argv) > 2 else 100)
        if min_size <= 0:
            raise ValueError
        
        code_caves = find_code_caves(filename, min_size)
        code_caves.sort(key=lambda x: x[1], reverse=True)

        os.system("cls" if os.name == "nt" else "clear")
        
        if len(code_caves) < 1:
            print(f"No code caves were found with a size of at least {min_size} bytes.")
        else:
            print("Address".ljust(12), "Size")
            print("-" * 20)
            for (address, size) in code_caves:
                print(str(address).ljust(12), f"{size}")
            print(f"\nFound {len(code_caves)} code caves with a minimum size of {min_size} bytes.")
    
    except IndexError:
        print("Error: Please specify the path to a file as the first argument.")
    
    except ValueError:
        print("Error: The minimum size of the code cave must be a number greater than 0.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' could not be found. Please specify a valid path to a file.")

    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory. Please specify a valid path to a file.")


main()
