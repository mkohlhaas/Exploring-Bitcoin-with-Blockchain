from CreateTransaction import OP_CHECKMULTISIG
from CreateTransaction import OP_CHECKSEQUENCEVERIFY, OP_CHECKSIG
from CreateTransaction import OP_DROP
from CreateTransaction import createVarInt
from CreateTransaction import OP_2
from CreateTransaction import OP_IF
from CreateTransaction import OP_ENDIF
from CreateTransaction import OP_ELSE


def createRedeemScript2_2_seqcheck(pubkey_l: list):
    redeem_script_b = bytes([OP_IF, OP_2])
    for pubkey in pubkey_l:  # Alice + Bob
        pubkey_b = bytes.fromhex(pubkey)
        redeem_script_b += createVarInt(len(pubkey_b)) + pubkey_b
    redeem_script_b += bytes([OP_2, OP_CHECKMULTISIG])
    redeem_script_b += bytes([OP_ELSE, 0x01,
                              105,  # after 105 blocks
                              OP_CHECKSEQUENCEVERIFY, OP_DROP])
    pubkey_b = bytes.fromhex(pubkey_l[0])  # Alice pubkey
    redeem_script_b += createVarInt(len(pubkey_b)) + pubkey_b
    redeem_script_b += bytes([OP_CHECKSIG, OP_ENDIF])
    return redeem_script_b
