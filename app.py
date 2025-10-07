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
    files = sys.argv[2:]
    for o in options:
        if o not in 'clmw':
            print(f"ccwc: Wrong usage option -- {o}")
            print("usage: ccwc [-clmw] [file ...]")
            sys.exit(1)
    values = {
        'l': [],
        'w': [],
        'm': []
    }
    for i,file in enumerate(files):
        # with open(file, 'r', encoding='utf-8') as f:
        #     lines = f.readlines()
        #     words = [word for line in lines for word in line.split()]
        # read file just once since file reads are expensive
        with open(file, 'rb') as f:
            data_bytes = f.read()
        if 'l' in options or 'w' in options:
            text = data_bytes.decode('utf-8')
            lines = text.splitlines(keepends=True)
            values['l'].append(len(lines))
            if 'w' in options:
                # words = [word for line in lines for word in line.split()] # this is a list comprehension, not memory-efficient
                # using a generator expression, calculate the length of each line in words and keep it adding to sum on the fly
                values['w'].append(sum(len(line.split()) for line in lines))
        if 'm' in options or 'c' in options:
            values['m'].append(len(data_bytes))

        # print output for one file
        output_parts = []
        if values['l']:
            output_parts.append(str(values['l'][i]))
        if values['w']:
            output_parts.append(str(values['w'][i]))
        if values['m']:
            output_parts.append(str(values['m'][i]))
        print('\t'.join(output_parts) + f'\t{file}')
    # print total figures if there's more than 1 file
    if len(files)>1:
        output_parts = []
        if values['l']:
            output_parts.append(str(sum(values['l'])))
        if values['w']:
            output_parts.append(str(sum(values['w'])))
        if values['m']:
            output_parts.append(str(sum(values['m'])))
        print('\t'.join(output_parts) + f'\ttotal')
        
    
    
            
