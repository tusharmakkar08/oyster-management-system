# __author__ = 'tusharmakkar08'

import collections
from enum import Enum


class TravelMode(Enum):
    TUBE = 1
    BUS = 2


class Zone(Enum):
    ZONE_1 = 1
    ZONE_2 = 2
    ZONE_3 = 3
    ZONE_4 = 4


DEFAULT_ZONE = Zone.ZONE_4  # Will take any unmentioned node as node with zone 4
DEFAULT_NODE = 'default'

BUS_JOURNEY_ZONE_RATES = collections.defaultdict(lambda: 1.8)
TUBE_JOURNEY_ZONE_RATES = {
    (1, 1): 2.5, (1, 2): 3, (1, 3): 3.2, (1, 4): 3.2,
    (2, 1): 3, (2, 2): 2, (2, 3): 2.25, (2, 4): 3.2,
    (3, 1): 3.2, (3, 2): 2.25, (3, 3): 2, (3, 4): 2.25,
    (4, 1): 3.2, (4, 2): 3.2, (4, 3): 2.25, (4, 4): 2,
}
LOCS = ['Holborn', 'Aldgate', "Earl’s Court", "Hammersmith", "Arsenal", "Wimbledon", DEFAULT_NODE]
NODE_TO_ZONE_DICT = {
    'Holborn': [Zone.ZONE_1.name], 'Aldgate': [Zone.ZONE_1.name], "Earl’s Court": [Zone.ZONE_1.name, Zone.ZONE_2.name],
    "Hammersmith": [Zone.ZONE_2.name], "Arsenal": [Zone.ZONE_2.name], "Wimbledon": [Zone.ZONE_3.name],
    DEFAULT_NODE: [Zone.ZONE_4.name]
}
