expression = input('Arithmetic Expression: ')
x = int(expression[0])
y = expression[2]
z = int(expression[4])

if y == "+":
    print(x+z)
elif y == "/":
    print(x/z)
elif y == "*":
    print(x*z)
elif y == "-":
    print(x-z)