import sys
from tabulate import tabulate

try: 
    if len(sys.argv) <2:
        raise Exception('Too Few Arguments')

    if not sys.argv[1].lower().endswith('.csv'):
        raise Exception('This is not a csv file')

    order = []

    with open(sys.argv[1]) as table:
        for line in table:
            order.append(line.split(","))

    print(tabulate(order, headers="firstrow", tablefmt='grid'))
    sys.exit(0)

except FileNotFoundError:
    print("File not found")
    sys.exit(1)

except Exception as text:
    print(text)
    sys.exit(1)