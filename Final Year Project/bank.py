#Bank file to create bank account of user

class Bank:
    def __init__(self, balance):
        if not balance:
            raise ValueError("Balance must be a positive number")
        self.balance = balance

def balance():
    bank = get_balance()
    print(f"Your balance is currently: {bank.balance}$")

#Get user balance via input function
def get_balance():
    balance = input("What is your account balance? ").strip()
    return Bank(balance)

if __name__ == "__main__":
    balance()