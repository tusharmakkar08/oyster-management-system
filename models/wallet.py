# __author__ = 'tusharmakkar08'


class Wallet:
    def __init__(self):
        self.amount = 0  # TODO: get init amount on the basis of user name from db

    def load_money(self, amount):
        self.amount += amount

    def deduct_money(self, amount):
        self.amount -= amount

    def get_money(self):
        return self.amount
