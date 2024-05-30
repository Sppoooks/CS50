import sys

line_counter = 0
   
try: 
    if len(sys.argv) <2:
        raise Exception('Too Few Arguments')

    if not sys.argv[1].lower().endswith('.py'):
        raise Exception('This is not a python file')

    with open(sys.argv[1],'r') as file, open('output.txt','w+') as output:
        for line in file:
            if line.strip() and not line.startswith('#'):
                output.write(line)
                line_counter += 1

    print(f"This document has {line_counter} lines")
    sys.exit(0)

except FileNotFoundError:
    print("File not found")
    sys.exit(1)

except Exception as text:
    print(text)
    sys.exit(1)
