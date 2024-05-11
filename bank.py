#Определите класс Account, имитирующий банковский счет. Класс должен включать атрибуты для
#хранения идентификации владельца, баланса счета и методы для депозита (пополнения) и снятия
#средтв, если на счету достаточно средтсвclass Account():

class Account():
    def __init__(self, id, balance=0):
         self.id = id
         self.balance = balance

    def deposit(self, money):
        if money >0:
          self.balance += money
          print(f"Вы успешно пополнили счет на {money} рублей. Сумма на счету - {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
           print(f"Недостаточно средств на счету")
        elif money <= self.balance:
             self.balance -= money
             print(f"Вы успешно сняли {money} рублей. Сумма на счету - {self.balance}")

    def all_balance(self):
        print(f"Текущий баланс - {self.balance}")

man = Account(id="123", balance=0)
man.deposit(600)
man.withdraw(100)
man.withdraw(200)
man.all_balance()
