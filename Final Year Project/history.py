import sqlite3

def purchase(account_number):
    con1 = sqlite3.connect("purchase_history.db")
    cur1 = con1.cursor()

    con2 = sqlite3.connect("useraccounts.db")
    cur2 = con2.cursor()


    sql_statement = f"SELECT First Last FROM accounts WHERE User_ID = {account_number}"
    res = cur2.execute(sql_statement)
    
    sql_statement = f"CREATE TABLE IF NOT EXIST {res.fetchall()[0] + res.fetchall()[1]}"
    cur1.execute(sql_statement)

if __name__ == "__main__":
    purchase(1)
