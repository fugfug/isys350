import bankaccount

def main():
    start_balance = float(input('enter starting balance: '))

    savings = bankaccount.BankAccount(start_balance)

    pay = float(input('how much were you paid this week: '))
    print('...')