

menu={"Baja Taco":4.00,
    "Burrito":7.50,
    "Bowl":8.50,
    "Nachos":11.00,
    "Quesadilla":8.5,
    "Super Burrito":8.5,
    "Super Quesadilla":9.50,
    "Taco":3.00,
    "Tortilla Salad":8.00,
    }
total_order = 0
while True:

    try:
        #user put order,prompting them for items
        order=input("item: ").title()
        if order in menu:
            total_order+=menu[order]
            print("Total: $", end="")
            print("{:.2f}".format(total_order))
        if order == "":
            break
    except EOFError:
        print()
        break