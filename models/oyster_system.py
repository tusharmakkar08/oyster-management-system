# __author__ = 'tusharmakkar08'

from functools import lru_cache

from models import user
from services import constants
from services.init_network import InitNetwork


class OysterSystem:
    def __init__(self, logger, draw_network=True):
        self.logger = logger
        self.bus_network, self.tube_network = InitNetwork(self.logger).init_bus_and_tube_network(draw_network)
        self.selected_network = {
            constants.TravelMode.BUS.name: self.bus_network,
            constants.TravelMode.TUBE.name: self.tube_network
        }

    @lru_cache()
    def _get_nodes(self, mode):
        node_object = self.selected_network[mode].get_graph().nodes()
        return {str(i): i for i in node_object}

    @staticmethod
    def add_and_get_user(name):
        user_obj = user.User(name)
        return user_obj

    def check_in(self, user_, node_name, mode):
        node_object = self._get_nodes(mode).get(node_name, self._get_nodes(mode)[constants.DEFAULT_NODE])
        user_.set_start_node(node_object)
        max_possible_price = self.selected_network[mode].get_max_weight_edge(node_object)
        user_.deduct_money(max_possible_price)

    def check_out(self, user_, node_name, mode):
        node_object = self._get_nodes(mode).get(node_name, self._get_nodes(mode)[constants.DEFAULT_NODE])
        max_possible_price = self.selected_network[mode].get_max_weight_edge(node_object)
        user_.add_money(max_possible_price)
        start_state = user_.get_start_node()
        actual_price = self.selected_network[mode].get_graph().get_edge_data(start_state, node_object)['weight']
        user_.deduct_money(actual_price)
        user_.set_start_node(None)
