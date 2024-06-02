#Create user info and save in csv file
import csv

class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last

def get_name():
    first = input("What is your first name? ")
    last = input("What is your last name? ")
    return User(first, last)

def user_name():
    name = get_name()
    print(f"First name: {name.first}")
    print(f"Last name: {name.last}")

if __name__ == "__main__":
    user_name()