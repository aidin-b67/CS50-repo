import re
import sys


def main():

    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        lists_of_numbers = ip.split(".")
        for numbers in lists_of_numbers:
            if int(numbers) < 0 or int(numbers) > 255:
                return False

        return True

    else:
        return False


if __name__ == "__main__":
    main()