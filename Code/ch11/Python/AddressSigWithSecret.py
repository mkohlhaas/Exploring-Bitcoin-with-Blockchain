from CreateTransaction import createVarInt
from CreateTransaction import OP_EQUALVERIFY
from CreateTransaction import OP_CHECKSEQUENCEVERIFY
from CreateTransaction import OP_CHECKSIG
from CreateTransaction import OP_DROP
from CreateTransaction import OP_SHA256
from CreateTransaction import OP_IF
from CreateTransaction import OP_ENDIF
from CreateTransaction import OP_ELSE


def createRedeemScriptWithSecretHash(pubkey_agency: str,
                                     pubkey_agent: str,
                                     secret_h: bytes):
    redeem_script_b = bytes([OP_IF, OP_SHA256])
    redeem_script_b += createVarInt(len(secret_h)) + secret_h
    redeem_script_b += bytes([OP_EQUALVERIFY])
    pubkey_b = bytes.fromhex(pubkey_agent)
    redeem_script_b += createVarInt(len(pubkey_b)) + pubkey_b
    redeem_script_b += bytes([OP_CHECKSIG])
    redeem_script_b += bytes([OP_ELSE, 0x01,
                              105,  # after 105 blocks
                              OP_CHECKSEQUENCEVERIFY, OP_DROP])
    pubkey_b = bytes.fromhex(pubkey_agency)
    redeem_script_b += createVarInt(len(pubkey_b)) + pubkey_b
    redeem_script_b += bytes([OP_CHECKSIG, OP_ENDIF])
    return redeem_script_b
