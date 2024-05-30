text = input("Camel text: ")
for s in text:
    if s.islower() == True:
        print(s, end="")
    elif s.isupper() == True:
        s = s.lower()
        print("_" + s, end="")