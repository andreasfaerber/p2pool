from p2pool.bitcoin import networks

PARENT = networks.nets['feathercoin_testnet']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 60*60//10 # shares
REAL_CHAIN_LENGTH = 60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 120 # blocks
IDENTIFIER = '4665617468657221'.decode('hex')
PREFIX = 'b131010ba6d4729a'.decode('hex')
P2P_PORT = 19340
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 19427
BOOTSTRAP_ADDRS = 'pool.maeh.org pool2.maeh.org'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
