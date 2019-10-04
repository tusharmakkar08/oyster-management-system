# __author__ = 'tusharmakkar08'

import matplotlib.pyplot as plt
import networkx as nx
import warnings

from models import base_network
from models.rate_card import RateCard
from services import constants as const

warnings.filterwarnings("ignore")


class InitNetwork:
    def __init__(self, logger):
        self.logger = logger
        self.nodes = const.LOCS
        self.zones = list(const.Zone.__members__)
        self.nodes_to_zones_dict = const.NODE_TO_ZONE_DICT
        self.mode_rate_dict = {
            const.TravelMode.TUBE.name: const.TUBE_JOURNEY_ZONE_RATES,
            const.TravelMode.BUS.name: const.BUS_JOURNEY_ZONE_RATES
        }

    @staticmethod
    def _set_network_edges(network, rate_card):
        network.add_edges(rate_card)
        return network

    @staticmethod
    def _draw_graph(network):
        nx.draw_networkx_edge_labels(network.get_graph(), nx.spring_layout(network.get_graph()),
                                     edge_labels=nx.get_edge_attributes(network.get_graph(), 'weight'))
        nx.draw_networkx(network.get_graph(), with_labels=True)
        plt.show()

    def _set_rate_card(self, rc_obj, mode):
        [rc_obj.set_rate(src_z, dst_z, self.mode_rate_dict[mode][(const.Zone[src_z].value, const.Zone[dst_z].value)])
         for dst_z in self.zones for src_z in self.zones]
        return rc_obj

    def _set_zones(self, network):
        [node.set_zones(self.nodes_to_zones_dict[node.name]) for node in network.get_graph().nodes()]
        return network

    def _set_network_nodes(self, network):
        network.add_nodes(self.nodes)
        return self._set_zones(network)

    def _init_network(self, mode, draw_network):
        rate_card = RateCard()
        rate_card = self._set_rate_card(rate_card, mode)
        base_network_ = base_network.BaseNetwork(mode)
        base_network_ = self._set_network_nodes(base_network_)
        self._set_network_edges(base_network_, rate_card)
        if draw_network:
            self._draw_graph(base_network_)
        return base_network_

    def init_bus_and_tube_network(self, draw_network):
        bus_network_ = self._init_network(const.TravelMode.BUS.name, draw_network)
        tube_network_ = self._init_network(const.TravelMode.TUBE.name, draw_network)
        return bus_network_, tube_network_
