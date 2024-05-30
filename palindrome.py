import sys

def check_palindrome(input, index = 0):
    if index > len(input)/2:
        print("String is a palindrome")
    elif input[index] == input[-1 * (index + 1)]:
        return check_palindrome(input, index + 1)
    else:
        print("String is not a palindrome")

check_palindrome(sys.argv[1])