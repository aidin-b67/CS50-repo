expression = input("expression: ")

x, y, z = expression.split(" ")

X = float(x)
Z = float(z)


if y == "+":
    result= X + Z

if y == "-":
    result = X - Z

if y == "*":
    result = X * Z

if y == "/":
    result= X / Z

print(round(result,1))