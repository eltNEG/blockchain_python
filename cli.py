# -*- coding: utf-8 -*-

"""blockchain.py

Usage:
  cli.py addblock -data <x>
  cli.py printchain

Options:
  -h --help     Show this screen.
  --version     Show version.
  -data         data to put in block


"""

import regex

from PyInquirer import style_from_dict, Token, prompt, print_json
from PyInquirer import Validator, ValidationError
from pprint import pprint

from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='blockchain 1.0.0')
    print(arguments)
