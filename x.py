string = input()

for character in string:
    if character.isalpha():
        if character.isupper():
            new = concat(character.lower())

print(new,end="\n")
