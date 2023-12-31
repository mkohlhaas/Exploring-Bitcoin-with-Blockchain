import mmap
import json
from SegwitCoinbaseTransaction import getCoinbaseTransactionInfo

if __name__ == '__main__':
    txn_b = bytes.fromhex('010000000001010000000000000000000000000000000000000'
                          '000000000000000000000000000ffffffff400360310a040e50'
                          '12602f706f6f6c696e2e636f6d2f746170726f6f742f6269703'
                          '92f57414aa61d1d79f4d92b134a2172611e120154741700bd36'
                          '220000000000ffffffff041d066c260000000017a9149837b6c'
                          'a944b36f71b94d19cf1e1acd179726424870000000000000000'
                          '266a24b9e11b6db14323c98fb36550f3bf4d5ce2ea5fcb878ec'
                          '778a849a99add2cc2e76141432b0000000000000000266a24aa'
                          '21a9ed1cb4ceb5ec7fef10b852514760a409539056be66601f5'
                          '89c5539e443fbbfdcfc00000000000000002b6a2952534b424c'
                          '4f434b3a68894f43c4cff546f6ee51f9e9475bcd2bfff279283'
                          'cb6de9fc47c2c002eb263012000000000000000000000000000'
                          '000000000000000000000000000000000000006b6066c1')
    txn_m = mmap.mmap(-1, len(txn_b) + 1)
    txn_m.write(txn_b)
    txn_m.seek(0)
    tx = getCoinbaseTransactionInfo(txn_m)
    print(json.dumps(tx))
