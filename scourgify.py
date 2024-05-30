import sys
import csv

try:
    if len(sys.argv) > 3:
        raise Exception("Too many arguments")

    if len(sys.argv) <= 2:
        raise Exception("Too few arguments")
    
    with open(sys.argv[1], 'r',newline='') as read_file, open(sys.argv[2],'w+',newline='') as write_file:
        for line in read_file:
            split_line = line.split(',')
            output_line = [element.strip('" ').rstrip() for element in split_line]
            print(output_line)
            row_write = csv.writer(write_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            row_write.writerow(output_line)         

except FileNotFoundError:
    print("File not found")
    sys.exit(1)

except Exception as text:
    print(text)
    sys.exit(1)
