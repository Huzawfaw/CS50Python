name = input("Name Please : ")

for letter in name:

    if letter.isupper() : letter = "_" + letter

    print (letter.lower(), end="")

print()
