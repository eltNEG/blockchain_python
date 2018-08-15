# -*- coding: utf-8 -*-

"""blockchain.py

Usage:
  cli.py addblock -data <data>
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
from pow import *


def add_block(data):
    bc.add_block(data)
    return "Success!"


def printchain():

    bci = bc.iterator
    bci.seek_to_first()
    print("------------ Chain Start ------------")
    while(True):
        try:
            block = bc.deserialize(bci.value())
            print("Prev. hash: %s\n" % (block.PrevBlockHash))
            print("Data: %s\n" % (block.Data))
            print("Hash: %s\n" % (block.Hash))
            pow = ProofOfWork(block)
            print("TargetBits: %s\n"%(block.Bits))
            print("PoW: %s\n" % (pow.validate(block)))
            bci.next()

        except:
            return "------------- Chain End --------------"


def Run(_blockchain):
    global bc
    bc = _blockchain
    arguments = docopt(__doc__, version='blockchain 1.0.0')
    if arguments['<data>']:
        print(add_block(arguments['<data>']))
    else:
        print(printchain())
