def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
# the vanity plate number should be between 2-6

       if len(s) < 2 or len(s) > 6:
        return False
#all vanity plates must start with at least two letter
       if s[0].isalpha() == False or s[1].isalpha() == False:
        return False



# middle number and last string can not be number
       i = 0
       while i < len(s):
            if s[i].isalpha() == False:
              if s[i] == '0':

                return False
              else:
                return True
            i += 1



       for c in s:
             if c in ["."," ","!","?"]:
                 return False
       return True

main()