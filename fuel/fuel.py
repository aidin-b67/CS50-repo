r
while True:
    f = input("Fraction: ")
    try:
     x, z = f.split("/")
     X = int(x)
     Z = int(z)
     F = X / Z
     if F <= 1.00:
           break

    except(ValueError,ZeroDivisionError):
     pass

p = round((F * 100))

if p <= 1 :
     print("E")

elif p >= 99:
   print("F")
else:
    print(f"{(p)}%")