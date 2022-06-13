import pytest

class Bank:
    def __init__(self):
        self.amount = 0

    def add_money(self, money: int):
        self.amount += money

    def withdraw_money(self, money):
        if money > self.amount:
            raise NotEnoughCash('Nie ma tyle pieniedzy')
        self.amount -= money

        return money
class NotEnoughCash(Exception):
    pass

class TestBank:
    def test_withdraw_over_amount(self):
        with pytest.raises(NotEnoughCash):
            bank = Bank()
            bank.withdraw_money(200)

