def main():
    answer = input("what time is it? ")
    time = convert(answer)

    if time >= 7 and time <= 8:
        print("breakfast time")

    elif time >= 12 and time <= 13:
        print("lunch time")

    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        exit

def convert(time):
    hours, minutes =time.split(":")
    Hours= float(hours)
    Minutes= round((float(minutes) / 60),1)
    return Hours + Minutes


if __name__ == "__main__":
    main()

