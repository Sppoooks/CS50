#Create user account
import csv

class User:
    def __init__(self, first, last, balance):
        self.first = first
        self.last = last
        self.balance = balance

def get_userinfo():
    first = input("What is your first name? ")
    last = input("What is your last name? ")
    balance = input("What is your account balance? ").strip()
    return User(first, last, balance)

def useraccount():
    write = get_userinfo()
    with open('fullnames.csv', 'w+', newline = '') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['First', 'Last', 'Balance'])
        writer.writerow([f'{write.first}', f'{write.last}', f'{write.balance}'])

if __name__ == "__main__":
    useraccount()