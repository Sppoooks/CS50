import sqlite3
import useraccount as user
import history

def main():
    #Connect to database
    con = sqlite3.connect("useraccounts.db")
    cur = con.cursor()
    _prompt = input("What would you like to do?\n1. Create account\n2. Choose from existing accounts\n")

    #Create new account or select existing account
    match _prompt:
        case "1":
            user.useraccountsql()
            sql_statement = f"SELECT * FROM accounts ORDER BY User_ID DESC LIMIT 1"
            res = cur.execute(sql_statement)
            account_number = int(res.fetchone()[0]) #Set account number to new account ID

        case "2":
            sql_statement = "SELECT User_ID, First, Last, Balance FROM accounts"
            res = cur.execute(sql_statement)
            for i in res.fetchall():
                print(f"{i[0]}. {i[1]} {i[2]}, {i[3]}$")
            #Select account ID
            account_number = input("Select account number\n")

    while True:
        #Prompt user for action
        _prompt = input("What would you like to do: \n1. Deposite \n2. Withdraw \n3. Make a Purchase\n4. View purchase history\n5. Exit\n")

        #Update balance of user
        match _prompt:
            case "1":
                amount = input("Amount: ")
                sql_statement = f"UPDATE accounts SET Balance = Balance + {int(amount)} WHERE User_ID = {account_number}"
                cur.execute(sql_statement)
                con.commit()

            case "2":
                amount = input("Amount: ")
                sql_statement = f"UPDATE accounts SET Balance = Balance - {int(amount)} WHERE User_ID = {account_number}"
                cur.execute(sql_statement)
                con.commit()

            case "3":
                #save purchase in db
                description = input("What would you like to purchase?\n")
                value = input("What is the cost of the purchase?\n")
                history.save_purchase(account_number, description, value)

                #update balance
                sql_statement = f"UPDATE accounts SET Balance = Balance - {int(value)} WHERE User_ID = {account_number}"
                cur.execute(sql_statement)
                con.commit()

            case "4":
                #print purchase history of account user
                history.view_history(account_number)

            case "5":
                #exit program
                break

        #Print new balance
        sql_statement = f"SELECT Balance FROM accounts WHERE User_ID = {account_number}"
        res = cur.execute(sql_statement)
        print(f"Your balance is: {res.fetchone()[0]}\n")
    con.close()

if __name__ == "__main__":
    main()