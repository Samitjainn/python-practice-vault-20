text = input("Enter a string: ")

i = 0
result = ""

while (i < len(text)):
    ch = text[i]

    if ch.isupper():
        result = result + ch.lower()
    elif ch.islower():
        result = result + ch.upper()
    else:
        result = result + ch

    i = i + 1

print("Converted string:", result)
