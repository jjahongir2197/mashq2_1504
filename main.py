class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "so'm qo'shildi")
        else:
            print("Noto'g'ri summa!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Pul yetarli emas!")
        elif amount <= 0:
            print("Noto'g'ri summa!")
        else:
            self.balance -= amount
            print(amount, "so'm yechildi")

    def show_balance(self):
        print(self.owner, "balansi:", self.balance)


def main():
    acc = BankAccount("Jahongir", 100000)

    acc.show_balance()

    acc.deposit(50000)
    acc.withdraw(30000)
    acc.withdraw(150000)

    acc.show_balance()


main()
