while True:
    try:
        x = input("Fraction: ")
        y = [int(x[0]), int(x[2])]
        percentage = (y[0]/y[1])*100
        if y[0] <= y[1]:
            break

    except ValueError:
        print("Please input a valid fraction")

    except ZeroDivisionError:
        print("Invalid, dividing by zero")

if y[0] < y[1] and y[0] != 0:
    print(round(percentage, 2), "%")

elif y[0] == y[1]:
    print("F")

elif y[0] == 0:
    print("E")