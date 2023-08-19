import mmap
import json
from SegwitBlockTransaction import getTransactionInfo

if __name__ == '__main__':
    txn_b = bytes.fromhex('02000000000102dc0f4a1601bd6bfec4241fede438bee459587'
                          '73fe5d95f88ec890e2363983e0c0100000000ffffffff904d74'
                          'd770c0ef5ce91190750b235d7ffb340b82b392812ba8e6ad5f0'
                          'a8c4ca70000000000ffffffff02f31f0a00000000001600140c'
                          '986c1d8ad520c072ee1aa0a151615c891ef71455b8180000000'
                          '000160014097e656deb55afa3786c600a87d990dcab86fc2d02'
                          '4730440220685234e91eb14e6d1717c543193181700b1cbf5fe'
                          'cddbee79ed9b6b0bbf24077022033dac5cc679dca810327dcac'
                          '4b84ba2b007a3a4fda6fb2cbc6099ae91c53804f01210277bed'
                          '123bc0c0f9883b0bc14014f0385d39eac7ac7212d8c9928fa41'
                          '21a191f4024730440220635eb52780098e3bd1e39a630a23f55'
                          '3ac62b97d0cd0356fa34ceb47cb0195250220599b83d8872ff1'
                          '73781b83b36bf159b59ed7685f73811f449fa1df814fbef15c0'
                          '121022cd4d498f1ed0ee382eefe4b6e1d8c5aa678d47b693389'
                          'ccdf77559b3220c5fa00000000')
    txn_m = mmap.mmap(-1, len(txn_b) + 1)
    txn_m.write(txn_b)
    txn_m.seek(0)
    tx = getTransactionInfo(txn_m)
    print(json.dumps(tx))
