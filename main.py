from blockchain import *
from cli import *

db_file = "/tmp/blockchain"

def main():
  bc = Blockchain("/tmp/blockchain").new_blockchain()
  Run(bc)
  bc.db.close()



main()
