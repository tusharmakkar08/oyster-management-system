# Oyster Card Problem

#### System Setup:

1. Language requirement: Python 3.5+ (Used Python 3.6)
2. Install virtualenv using `pip install virtualenv`
3. Create virtualenv using `virtualenv -p python3 venv`
4. Activate virtualenv using `source venv/bin/activate`
5. Run `pip install -r requirements.txt`
6. Run ``export PYTHONPATH=`pwd` ``

#### Running instruction:

###### Running code:
Do `cd services`. Run `python main_service.py`.
It will initialize graphs and draw them (Would need to close them
before proceeding or alternatively pass `draw_graph`=False).
After that it will print the result on terminal.

###### Running tests:
Go to oyster home directory.
Run `py.test --cov=models/ --cov=services/ --disable-pytest-warnings`.
Run `coverage html` to generate html report which can be found
in `html_cov`.

#### Source code explanation:

I have tried writing code that this part is not needed.
In case this is required, here it is:

I have divided the code into 2 parts:

1. *Models*: Crux of the code. Has all the necessary components to build
a generic system like Oyster.
2. *Services*: Specification for oyster system.
It has network initialization, user creation and constants related to
Oyster.

###### Models:

1. *base_network.py*: Base class for `networkx` network generation.
Generates edge and node corresponding to it.
2. *oyster_system.py*: Main system file. Bus and Tube Networks are
components of it. User is created using it. User checks in and checks
out from this system.
3. *user.py*: User class. User has a wallet.
4. *wallet.py*: Wallet class.
5. *rate_card.py*: Rate card class for network weights.

###### Services:

1. *constants.py*: Fixed mappings, rates, modes and other constants.
2. *init_network.py*: Initializes bus and tube network for oyster using
constants.
3. *main_service.py*: Initializes oyster_system, networks and users.
Sample transaction is carried out here.

#### TODO:

1. Added TODO's in the code.
2. Better exception handling and fail-safe code building.
(something like insufficient balance in the wallet)
3. Better integration and unit tests.
4. Add comments in code.
5. Haven't followed TDD here.

#### Stats:

For models number of line of code:

      42 ./oyster_system.py
      25 ./user.py
      59 ./base_network.py
      12 ./rate_card.py
       1 ./__init__.py
      15 ./wallet.py
     154 total

For service number of line of code:

      62 ./init_network.py
      34 ./constants.py
       1 ./__init__.py
      38 ./main_service.py
     135 total

For tests number of line of code:

      77 ./test_oyster_system.py
       1 ./__init__.py
      78 total

For coverage:

    tests/test_oyster_system.py .........                                                                                                                              [100%]

    ---------- coverage: platform darwin, python 3.6.0-final-0 -----------
    Name                       Stmts   Miss  Cover
    ----------------------------------------------
    models/__init__.py             0      0   100%
    models/base_network.py        34      0   100%
    models/oyster_system.py       28      0   100%
    models/rate_card.py            7      0   100%
    models/user.py                16      0   100%
    models/wallet.py               9      0   100%
    services/__init__.py           0      0   100%
    services/constants.py         16      0   100%
    services/init_network.py      43      4    91%
    services/main_service.py      29     29     0%
    ----------------------------------------------
    TOTAL                        182     33    82%
