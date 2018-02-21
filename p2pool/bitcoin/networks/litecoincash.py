import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'c7e4baf8'.decode('hex')
P2P_PORT = 62458
ADDRESS_VERSION = 28
RPC_PORT = 62457
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_block_header(bitcoind, '12a765e31ffd4059bada1e25190f6e98c99d9714d334efa41a195a7e7e04bfe2')) and # genesis block
            (yield helper.check_block_header(bitcoind, '00000000de1e4e93317241177b5f1d72fc151c6e76815e9b0be4961dfd309d60')) and # LitecoinCash: Premine block
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000*10 >> (height + 1)//840000
POW_FUNC = data.hash256
BLOCK_PERIOD = 150 # s
SYMBOL = 'LCC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'LitecoinCash') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/LitecoinCash/') if platform.system() == 'Darwin' else os.path.expanduser('~/.litecoincash'), 'litecoincash.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://explorer.litecoinca.sh/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://explorer.litecoinca.sh/address/'
TX_EXPLORER_URL_PREFIX = 'https://explorer.litecoinca.sh/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
