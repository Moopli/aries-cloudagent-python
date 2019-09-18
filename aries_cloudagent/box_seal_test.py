#!/usr/bin/env python3

from .wallet import crypto
from .wallet.util import b64_to_bytes, b58_to_bytes, bytes_to_b58
import nacl.bindings


def make_seed(data: bytes):
	seed = bytearray(nacl.bindings.crypto_sign_SEEDBYTES)
	seed[:len(data)] = data[:len(seed)]
	seed = bytes(seed)
	# print(len(seed) - nacl.bindings.crypto_sign_SEEDBYTES)
	return seed

seed = make_seed("alice".encode())

pkSign, skSign = nacl.bindings.crypto_sign_seed_keypair(seed)

# Generating a Recipient key pair for testcases
print("PK (Ed): ", bytes_to_b58(pkSign))
print("SK (Ed): ", bytes_to_b58(skSign))

pkSeal = nacl.bindings.crypto_sign_ed25519_pk_to_curve25519(pkSign)
skSeal = nacl.bindings.crypto_sign_ed25519_sk_to_curve25519(skSign)

print("PK (Curve): ", bytes_to_b58(pkSeal))
print("SK (Curve): ", bytes_to_b58(skSeal))

# Paste in b64url data
msg_in = "oxjRLcgYSHVOlgzBdBHyTRZtKAGWF7ZVbAnWy_ZnPSC4joMVWgMxkmPSdH1qXK3B8S1plCHSVP-quMqoLlJmB4ZErhX3HuQmGq8dBlxIHmxjVVxMQU77o4TIp1rtMR8_denZqsPAUQ=="

msg_in = b64_to_bytes(msg_in, urlsafe=True)

msg_out = nacl.bindings.crypto_box_seal_open(msg_in, pkSeal, skSeal)

print(msg_out.decode("ascii"))
