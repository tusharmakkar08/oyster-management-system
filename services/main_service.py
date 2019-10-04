# __author__ = 'tusharmakkar08'

import logging

from models import oyster_system
from services import constants


class MainService:
    def __init__(self, logger):
        self.logger = logger
        self.oyster_system_obj = oyster_system.OysterSystem(self.logger)

    def run(self):
        sample_user = self.oyster_system_obj.add_and_get_user('Alef Education')
        self.logger.info('Before Loading - Money in Wallet is %s' % sample_user.get_money())
        sample_user.add_money(30)
        self.logger.info('After Loading - Money in Wallet is %s' % sample_user.get_money())
        self.oyster_system_obj.check_in(sample_user, 'Holborn', constants.TravelMode.TUBE.name)
        self.logger.info('After Check in Holborn tube - Money in Wallet is %s' % sample_user.get_money())
        self.oyster_system_obj.check_out(sample_user, "Earl’s Court", constants.TravelMode.TUBE.name)
        self.logger.info('After Check out Earl Court tube - Money in Wallet is %s' % sample_user.get_money())
        self.oyster_system_obj.check_in(sample_user, 'Earl’s Court', constants.TravelMode.BUS.name)
        self.logger.info('After Check in Earl court bus - Money in Wallet is %s' % sample_user.get_money())
        self.oyster_system_obj.check_out(sample_user, "Chelsea", constants.TravelMode.BUS.name)
        self.logger.info('After Check out Chelsea bus - Money in Wallet is %s' % sample_user.get_money())
        self.oyster_system_obj.check_in(sample_user, 'Earl’s Court', constants.TravelMode.TUBE.name)
        self.logger.info('After Check in Earl court tube - Money in Wallet is %s' % sample_user.get_money())
        self.oyster_system_obj.check_out(sample_user, "Hammersmith", constants.TravelMode.TUBE.name)
        self.logger.info('After Check out Hammersmith tube - Money in Wallet is %s' % sample_user.get_money())


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s][%(threadName)s][%(process)d] ~ %(name)s "
                               "{%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    lgr = logging.getLogger('init_service')
    lgr.setLevel(2)
    MainService(lgr).run()
