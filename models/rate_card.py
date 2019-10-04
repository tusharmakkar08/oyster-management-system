# __author__ = 'tusharmakkar08'


class RateCard:
    def __init__(self):
        self.rate_card = {}  # TODO: Based on vehicle type get rate from db

    def set_rate(self, src_zone, dst_zone, amount):
        self.rate_card[(src_zone, dst_zone)] = amount

    def get_rate(self, src_zone, dst_zone):
        return self.rate_card[(src_zone, dst_zone)]
