import sqlite3

def get_username(account_number):
    #connect to user account database
    con = sqlite3.connect("useraccounts.db")
    cur = con.cursor()

    #select which user to input purchase history
    sql_statement = f"SELECT First, Last FROM accounts WHERE User_ID = {account_number}"
    res = cur.execute(sql_statement)

    #format account username
    username = res.fetchall()[0]
    username = f"{username[0]} {username[1]}"
    return username


def save_purchase(account_number, description, value):

    #create or connect purchase history database file
    con = sqlite3.connect("purchase_history.db")
    cur = con.cursor()

    username = get_username(account_number)

    #create table for user if it doesn't exist
    sql_statement = f"CREATE TABLE IF NOT EXISTS '{username}' (Description text, Value integer)"
    cur.execute(sql_statement)

    #input description and value or purchase into db
    data = (description, value)
    cur.execute(f"INSERT INTO '{username}' (Description, Value) VALUES (?, ?)", data)
    con.commit()
    con.close()

    print("Your purchase has been logged")

def view_history(account_number):

    #connect to purchase history
    con = sqlite3.connect("purchase_history.db")
    cur = con.cursor()

    username = get_username(account_number)

    #try to print all purchases registered
    try:
        sql_statement = f"SELECT * FROM '{username}'"
        res = cur.execute(sql_statement)
        for i in res.fetchall():
            print(f"{i[0]}, {i[1]}")

    except Exception as text:
        print(f"{username} has made no purchases")


if __name__ == "__main__":
    view_history(2)