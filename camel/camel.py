# get user input
camelcase=input ("camelCase : " )

#print"snake_case
print("snake_case: ", end="")

#loop through every letter
for letter in camelcase:

        # check if letter is upper case
    if letter . isupper() :
        #print underscorea and the letter in lower case
         print("_" + letter.lower(), end="")






        #otherwise print letter
    else:
        print(letter,end="")

# print space in the end
print()