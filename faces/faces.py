def main():
    # get user input
    message = input()
    # call convert function
    result = convert(message)
    #print the result
    print(result)


def convert(message):
    #Replace :) for happy emoji
    message1 = message.replace(":)",'🙂')
    #Replace :( for sad emoji
    message2 = message1.replace(":(",'🙁')
    # return string
    return message2

main()