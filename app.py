import sys
import re

files = sys.argv[1:]

# Program use cases:
# A -  If no options are provided, print number of lines, words and bytes from the 
# list of files 
# B - Options are provided 
# 1. Read from a file
# 2. Read from standard input
# 3. Read from multiple files

def read_from_one_file(file):
    return 0
# Main program
# If no options are provided:

if '-' not in sys.argv[1]:
    total = {
            "lines": 0,
            "words": 0,
            "bytes": 0
        }
    for file in files:
        # see if file exists in current directory
        try:
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            with open(file, "rb") as f:
                data_bytes = f.read()
        except FileNotFoundError:
            print(f"{file}: No such file or directory.")
        except PermissionError:
            print(f"{file}: Permission is not granted to read. ")
        except Exception as e:
            print(f"{file}: Unexpected error in reading file. {e=}, {type(e)=}" )
        # Process lines from file
        words = [word for line in lines for word in line.split()]
        # Print output
        print(f"{len(lines)}\t{len(words)}\t{len(data_bytes)}\t{file}")
        total["lines"] = total["lines"] + len(lines)
        total["words"] = total["words"] + len(words)
        total["bytes"] = total["bytes"] + len(data_bytes)
    if len(files)>1:
        print(f"{total["lines"]}\t{total["words"]}\t{total["bytes"]}\ttotal")
else:
    options = sys.argv[1].lstrip('-')
    print(options)
