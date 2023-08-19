#defining the input value for date
months= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
comma = ","
while True:

    date = input("Date: ")

    try:
        month, day, year = date.split("/")
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break

    except:
        try:
            old_month, old_day, year = date.split(" ")

            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1

            if comma in old_day:
             day = old_day.replace(",","")


            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
              break

        except:
          pass

print(f"{year.strip()}-{int(month):02}-{int(day):02}")
