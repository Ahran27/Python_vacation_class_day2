class BankAccount:
    def __init__(self,owner,balance = 0):#만들어진 애들의 초깃값은 0이라는 것을 정의
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount #입금된 금액
        print(f"{self.owner}님의 계좌로 {amount}원 입금되었습니다. 현재 잔액 : {self.balance}")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount#출금금액은 입력된 값을 기존 값에서 뺀 것
            print(f"{self.owner}님의 계좌에서 {amount}원을 출금하였습니다. 현재 잔액 : {self.balance}")
        else:
            print("잔액이 부족합니다.")

    def check_balance(self):
        print(f"{self.owner}님의 현재 계좌 잔액 {self.balance}원")

bank1 = BankAccount("ahran kim",10000)
bank1.check_balance()
bank1.deposit(1000000)
bank1.check_balance()
bank1.withdraw(50000)
bank1.check_balance()

bank2 = BankAccount("Tim",10000000000000)
bank2.check_balance()