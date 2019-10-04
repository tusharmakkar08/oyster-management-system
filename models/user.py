# __author__ = 'tusharmakkar08'

from models.wallet import Wallet


class User:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet()
        self.start_node = None

    def set_start_node(self, node):
        self.start_node = node

    def get_start_node(self):
        return self.start_node

    def add_money(self, amount):
        self.wallet.load_money(amount)

    def deduct_money(self, amount):
        self.wallet.deduct_money(amount)

    def get_money(self):
        return self.wallet.get_money()
