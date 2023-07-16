import mysql.connector
import decimal

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bank"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Function to create a new bank account
def create_account():
    name = input("Enter your name: ")
    balance = float(input("Enter initial balance: "))

    # Insert account details into the database
    insert_query = "INSERT INTO accounts (name, balance) VALUES (%s, %s)"
    values = (name, balance)
    cursor.execute(insert_query, values)
    db.commit()

    print("Account created successfully!")

# Function to deposit money into an account
def deposit():
    account_id = int(input("Enter account ID: "))
    amount = decimal.Decimal(input("Enter amount to deposit: "))

    # Check if the account exists
    select_query = "SELECT * FROM accounts WHERE id = %s"
    cursor.execute(select_query, (account_id,))
    account = cursor.fetchone()

    if account is not None:
        # Update the account balance
        new_balance = account[2] + amount
        update_query = "UPDATE accounts SET balance = %s WHERE id = %s"
        cursor.execute(update_query, (new_balance, account_id))
        db.commit()

        print("Deposit successful!")
    else:
        print("Account not found!")

# Function to withdraw money from an account
def withdraw():
    account_id = int(input("Enter account ID: "))
    amount = decimal.Decimal(input("Enter amount to withdraw: "))

    # Check if the account exists
    select_query = "SELECT * FROM accounts WHERE id = %s"
    cursor.execute(select_query, (account_id,))
    account = cursor.fetchone()

    if account is not None:
        if account[2] >= amount:
            # Update the account balance
            new_balance = account[2] - amount
            update_query = "UPDATE accounts SET balance = %s WHERE id = %s"
            cursor.execute(update_query, (new_balance, account_id))
            db.commit()

            print("Withdrawal successful!")
        else:
            print("Insufficient funds!")
    else:
        print("Account not found!")

# Function to display the account details
def display_account():
    account_id = int(input("Enter account ID: "))

    # Check if the account exists
    select_query = "SELECT * FROM accounts WHERE id = %s"
    cursor.execute(select_query, (account_id,))
    account = cursor.fetchone()

    if account is not None:
        print("Account ID:", account[0])
        print("Name:", account[1])
        print("Balance:", account[2])
    else:
        print("Account not found!")

# Main menu
while True:
    print("\nBank Management System")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        display_account()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")

# Close the database connection
db.close()