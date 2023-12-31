from CreateTransaction import createSignedTransaction
from CreateTransaction import getSignaturesAndExecScripts
from ParseScriptSig import SIGHASH_ANYONECANPAY, SIGHASH_NONE


def createTransactionStruct():
    txn = {}
    txn['version'] = 1
    txn['input_count'] = 1
    txn['inputs'] = []
    input0 = {}
    input0['prevtxn'] = \
        '5efcf04e32f061b9c4894f5b3a59fb3d8c5c56a6e7340b89b3a1a9ebacca998f'
    input0['prevtxnindex'] = 0
    input0['script_type'] = 'P2PKH'
    input0['privkeys'] = [
        'KwfxnwxpPG1RmhU8jaU8Ron4m1KZGymLAFNaMnSTonoZ7AQfnV53'
    ]
    input0['script_pubkey'] = \
        '76a91481d7033c19dcec645cb3f86ce41678756850ba4d88ac'
    input0['hash_type'] = SIGHASH_ANYONECANPAY | SIGHASH_NONE
    txn['inputs'].append(input0)
    txn['out_count'] = 0
    txn['locktime'] = 0
    return txn


if __name__ == '__main__':
    txn_struct = createTransactionStruct()
    txn_struct, signgrp_l, script_l = getSignaturesAndExecScripts(txn_struct)
    signed_txn_b = createSignedTransaction(txn_struct,
                                           signgrp_l,
                                           script_l)
    print(signed_txn_b.hex())
