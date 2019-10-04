# __author__ = 'tusharmakkar08'

import logging
import unittest

from models.oyster_system import OysterSystem
from services import constants


class TestOysterSystem(unittest.TestCase):
    def setUp(self):
        logger = logging.getLogger('test_oyster')
        self.oyster_system_obj = OysterSystem(logger, draw_network=False)

    def test_user_empty_wallet_creation(self):
        user = self.oyster_system_obj.add_and_get_user('test')
        self.assertEqual(user.get_money(), 0)

    def test_user_check_in_given_station_tube(self):
        user = self.oyster_system_obj.add_and_get_user('test')
        self.oyster_system_obj.check_in(user, 'Arsenal', constants.TravelMode.TUBE.name)
        self.assertEqual(user.get_money(), -3.2)
        user.add_money(10)
        self.assertEqual(user.get_money(), 6.8)

    def test_user_check_out_given_station_tube(self):
        user = self.oyster_system_obj.add_and_get_user('test')
        user.add_money(100)
        self.oyster_system_obj.check_in(user, 'Wimbledon', constants.TravelMode.TUBE.name)
        self.assertEqual(user.get_money(), 96.8)
        self.oyster_system_obj.check_out(user, 'Wimbledon', constants.TravelMode.TUBE.name)
        self.assertEqual(user.get_money(), 98)

    def test_user_check_in_not_given_station_tube(self):
        user = self.oyster_system_obj.add_and_get_user('test')
        self.oyster_system_obj.check_in(user, 'abc', constants.TravelMode.TUBE.name)
        self.assertEqual(user.get_money(), -3.2)
        user.add_money(10)
        self.assertEqual(user.get_money(), 6.8)

    def test_user_check_out_not_given_station_tube(self):
        user = self.oyster_system_obj.add_and_get_user('test')
        user.add_money(100)
        self.oyster_system_obj.check_in(user, 'Wimbledon', constants.TravelMode.TUBE.name)
        self.assertEqual(user.get_money(), 96.8)
        self.oyster_system_obj.check_out(user, 'abc', constants.TravelMode.TUBE.name)
        self.assertEqual(user.get_money(), 97.75)

    def test_user_check_in_given_station_bus(self):
        user = self.oyster_system_obj.add_and_get_user('test')
        self.oyster_system_obj.check_in(user, 'Arsenal', constants.TravelMode.BUS.name)
        self.assertEqual(user.get_money(), -1.8)
        user.add_money(10)
        self.assertEqual(user.get_money(), 8.2)

    def test_user_check_out_given_station_bus(self):
        user = self.oyster_system_obj.add_and_get_user('test')
        user.add_money(100)
        self.oyster_system_obj.check_in(user, 'Wimbledon', constants.TravelMode.BUS.name)
        self.assertEqual(user.get_money(), 98.2)
        self.oyster_system_obj.check_out(user, 'Wimbledon', constants.TravelMode.BUS.name)
        self.assertEqual(user.get_money(), 98.2)

    def test_user_check_in_not_given_station_bus(self):
        user = self.oyster_system_obj.add_and_get_user('test')
        self.oyster_system_obj.check_in(user, 'abc', constants.TravelMode.BUS.name)
        self.assertEqual(user.get_money(), -1.8)
        user.add_money(10)
        self.assertEqual(user.get_money(), 8.2)

    def test_user_check_out_not_given_station_bus(self):
        user = self.oyster_system_obj.add_and_get_user('test')
        user.add_money(100)
        self.oyster_system_obj.check_in(user, 'Wimbledon', constants.TravelMode.BUS.name)
        self.assertEqual(user.get_money(), 98.2)
        self.oyster_system_obj.check_out(user, 'abc', constants.TravelMode.BUS.name)
        self.assertEqual(user.get_money(), 98.2)
