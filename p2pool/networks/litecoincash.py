from p2pool.bitcoin import networks

PARENT = networks.nets['litecoincash']
SHARE_PERIOD = 25 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 7 # blocks
IDENTIFIER = '1c01746cfe4641d3'.decode('hex')
PREFIX = '1c01746cfeded854'.decode('hex')
P2P_PORT = 5054
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = True
WORKER_PORT = 5055
BOOTSTRAP_ADDRS = 'crypto.office-on-the.net siberia.mine.nu'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-lcc'
VERSION_CHECK = lambda v: None if 150001 <= v else 'LitecoinCash version too old. Upgrade to 0.15.0.1 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 3301
NEW_MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 33
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
