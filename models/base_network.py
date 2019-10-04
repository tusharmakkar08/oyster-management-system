# __author__ = 'tusharmakkar08'

import sys

from functools import lru_cache
from networkx import DiGraph


class BaseNode:
    def __init__(self, name, zones=()):
        self.name = name
        self.zones = zones

    def get_zones(self):
        return self.zones

    def set_zones(self, zones):
        self.zones = zones

    def __repr__(self):
        return self.name


class BaseNetwork:
    def __init__(self, name):
        self.name = name
        self._graph = DiGraph()

    @staticmethod
    def _find_user_min_rate(rate_card, src_node, dst_node):
        rate_to_charge = sys.maxsize
        for src_zone in src_node.get_zones():
            for dst_zone in dst_node.get_zones():
                rate_to_charge = min(rate_card.get_rate(src_zone, dst_zone), rate_to_charge)
        return rate_to_charge

    @lru_cache()
    def get_max_weight_edge(self, node):
        max_possible_price = 0
        for ind_edge in self._graph.edges.data('weight', nbunch=node):
            max_possible_price = max(max_possible_price, ind_edge[-1])
        return max_possible_price

    def get_graph(self):
        return self._graph

    def add_edges(self, rate_card):
        [self._graph.add_edge(src_node, dst_node, weight=self._find_user_min_rate(rate_card, src_node, dst_node))
         for dst_node in self._graph.nodes() for src_node in self._graph.nodes()]

    def add_nodes(self, nodes):
        self._graph.add_nodes_from([BaseNode(node) for node in nodes])
