# Bank Management System

## TODO: Define Classes

### TODO: Bank Class
# Attributes: name, location, list_of_accounts, list_of_customers
# Methods: add_account(account), remove_account(account), add_customer(customer), remove_customer(customer), display_accounts(), display_customers()

### TODO: Account Class
# Attributes: account_number, customer, balance
# Methods: deposit(amount), withdraw(amount), display_balance()

### TODO: Customer Class
# Attributes: name, contact_info, accounts
# Methods: update_contact_info(info), display_info()

### TODO: Transaction Class
# Attributes: account, customer, transaction_date, transaction_type, amount
# Methods: None (attributes to record transaction details)

## TODO: Define Class Relationships

### TODO: Bank
# Relationship: A Bank has a list of accounts and customers.

### TODO: Account
# Relationship: An Account belongs to a Bank and a Customer.
# Relationship: An Account can have multiple Transactions.

### TODO: Customer
# Relationship: A Customer is associated with a Bank and has multiple Accounts.
# Relationship: A Customer can update their contact info.

### TODO: Transaction
# Relationship: A Transaction involves a specific Account and Customer.

## TODO: Implement Methods and Attributes

### TODO: Bank Class
# Method: add_account(account) - Adds an account to the list_of_accounts.
# Method: remove_account(account) - Removes an account from the list_of_accounts.
# Method: add_customer(customer) - Adds a customer to the list_of_customers.
# Method: remove_customer(customer) - Removes a customer from the list_of_customers.
# Method: display_accounts() - Displays information about accounts.
# Method: display_customers() - Displays information about customers.

### TODO: Account Class
# Method: deposit(amount) - Adds an amount to the balance.
# Method: withdraw(amount) - Subtracts an amount from the balance.
# Method: display_balance() - Displays the current balance.

### TODO: Customer Class
# Method: update_contact_info(info) - Updates the contact_info attribute.
# Method: display_info() - Displays detailed information about the customer.

### TODO: Transaction Class
# Attributes: Holds attributes for account, customer, transaction_date, transaction_type, amount.

## TODO: Additional Steps

# Create instances of Bank, Account, and Customer classes to simulate interactions.
# Implement user interfaces to interact with the bank system.
# Add error handling to ensure smooth execution and user-friendly experience.
# Implement data persistence using file handling or a database.
# Write comprehensive unit tests to validate class methods.
# Create clear and concise documentation explaining class purpose and usage.
# Summarize project goals and how it demonstrates understanding of OOP concepts.
# Conclude the project description with a thank you or final thoughts.

class Bank:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.list_of_accounts = []


    def add_account(self,account):
        self.list_of_accounts.append(account)

    def remove_account(self,account):
        self.list_of_accounts.remove(account)

    def list_account(self):
        for account in self.list_of_accounts:
            print(f"{account.user}->{account.account_number}")

class Account:
    def __init__(self,account_number,user):
        self.account_number = account_number
        self.user = user

bank1 = Bank("Pan","Earth")
user1 = Account(1234,"Admin")
bank1.add_account(user1)
bank1.list_account()