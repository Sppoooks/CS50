def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
            
def is_valid(s):
    if s[:2].isalpha() and 2<=len(s)<=6 and s[-1].isdigit() == False and s[2] != "0" and s.isalnum():
        return True
    else:
        return False

main()