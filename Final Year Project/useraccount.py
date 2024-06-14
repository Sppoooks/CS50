#Create user account
import sqlite3

class User:
    def __init__(self, first, last, balance):
        self.first = first
        self.last = last
        self.balance = balance

def get_userinfo():
    first = input("What is your first name? ").title().strip()
    last = input("What is your last name? ").title().strip()
    balance = input("What is your account balance? ").strip()
    return User(first, last, balance)

def useraccountsql():

    user_info = get_userinfo()
    con = sqlite3.connect("useraccounts.db")
    cur = con.cursor()

    #reset database table if wanted
    # prompt = input("Clear table? y/n ")
    # if prompt == "y":
    #     sql_statement = "DELETE FROM accounts"
    #     cur.execute(sql_statement)
    # else:
    #     pass

    sql_statement = "CREATE TABLE IF NOT EXISTS accounts (User_ID integer PRIMARY KEY AUTOINCREMENT, First text, Last text, Balance integer)" #Create table if it doesn't exist
    cur.execute(sql_statement)
    
    data = (str(user_info.first), str(user_info.last), str(user_info.balance))
    cur.execute("INSERT INTO accounts(First, Last, Balance) VALUES (?, ?, ?)", data)
    con.commit() #commit input values into table
    con.close()

if __name__ == "__main__":
    useraccountsql()