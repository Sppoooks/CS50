import sqlite3

def purchase(account_number, description, value):

    #create or conenct purchase history database file
    con1 = sqlite3.connect("purchase_history.db")
    cur1 = con1.cursor()

    #connect to user account database
    con2 = sqlite3.connect("useraccounts.db")
    cur2 = con2.cursor()

    #select which user to input purchase history
    sql_statement = f"SELECT First, Last FROM accounts WHERE User_ID = {account_number}"
    res = cur2.execute(sql_statement)

    username = res.fetchall()[0]
    username = f"{username[0]} {username[1]}"

    #create table for user if it doesn't exist
    sql_statement = f"CREATE TABLE IF NOT EXISTS '{username}' (Description text, Value integer)"
    cur1.execute(sql_statement)

    data = (description, value)
    cur1.execute(f"INSERT INTO '{username}' (Description, Value) VALUES (?, ?)", data)
    con1.commit()




if __name__ == "__main__":
    purchase(1, "apple", 2000)