#!/usr/bin/env python

import json
import sys

sys.path.append('src')
import bitcoin

with open('src/testdata.json', 'r') as f:
    testdata = json.load(f)
    for timeproof in testdata['bitcoinproof']:
        assert bitcoin.b58encode(bitcoin.publickey_to_address(timeproof['data'])) == timeproof['addr']
    for hr in testdata['human-readable']:
        assert bitcoin.hash_to_hr_addresses('SHA256', hr['sha256']) == hr['addr']
    for addr in testdata['addresses']:
        b = ''.join(chr(int(addr['hex'][i:i + 2], 16)) for i in xrange(0, len(addr['hex']), 2))
        assert bitcoin.ripemd160_to_address(b[1:-4]) == b
        assert bitcoin.b58encode(b) == addr['base58']
        assert bitcoin.b58decode(addr['base58']) == b
        assert bitcoin.b58encode_nolong(b) == addr['base58']
        assert bitcoin.b58decode_nolong(addr['base58']) == b
    print 'OK'
