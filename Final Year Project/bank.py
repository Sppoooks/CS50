import sqlite3
import useraccount as user
class Bank:
    def __init__(self, deposit, withdraw):
        self.deposit = deposit
        self.withdraw = withdraw

def bank():
    con = sqlite3.connect("useraccounts.db")
    cur = con.cursor()
    _prompt = input("What would you like to do?\n1. Create account\n2. Choose from existing accounts\n")
    match _prompt:
        case "1":
            user.useraccountsql()
        case "2":
            sql_statement = "SELECT First, Last FROM accounts"
            res = cur.execute(sql_statement)
            print(res.fetchall())

    # _prompt = input("What would you like to do: \n1. Deposite \n2. Withdraw \n")
    # amount = input("Amount: ")
    # match _prompt:
    #     case "1":
    #         sql_statement: "UPDATE accounts "
    #     case "2":

if __name__ == "__main__":
    bank()