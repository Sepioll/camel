# prompts the user for the name of a variable in camel case
camelCase = input("camelCase: ")
# printing name in snake case.
print("snake_case: ", end="")

# looping
for letter in camelCase:

# is this upper letter?
    if letter.isupper():
        print("_" + letter.lower(), end="")
# if something else
    else:
        print(letter, end="")