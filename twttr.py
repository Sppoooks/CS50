text = input("Input string: ")
excluded = ["a", "e", "i", "o", "u"]

for letter in text:
    if letter in excluded:
        print("", end = "")
    else:
        print(letter, end = "")
        