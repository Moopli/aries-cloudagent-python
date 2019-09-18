#!/usr/bin/env python3

from .wallet import crypto
from .wallet.util import  bytes_to_b58, bytes_to_b64, b64_to_bytes, b58_to_bytes
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


# Current recipient keypair used in testcase

## PASTE DATA ##
b58_pub = "EGJzjnQCJZWxww4gn9SJt6UNNrCmBkNqmCvG29VLi3pX"
b58_priv = "5H2CB3nkxX1UiVVbE7sG6en6NXp1zPzYTzfBMU4ncCm9XMVcRrHw1anqRcGJ4xoSkpjCUVTz4jALSrVeiDC9tdyD"
msg_in = """{"protected":"eyJlbmMiOiJjaGFjaGEyMHBvbHkxMzA1X2lldGYiLCJ0eXAiOiJKV00vMS4wIiwiYWxnIjoiQXV0aGNyeXB0IiwicmVjaXBpZW50cyI6W3siZW5jcnlwdGVkX2tleSI6Ijh0NHFWWl9LRFpSX3F3OHlCOVJwUUdyMElQeGdOSVJKR1VlNGxNRUxranljN2xibHBtdmhjWkprb3JWcm5GSV8iLCJoZWFkZXIiOnsia2lkIjoiRUdKempuUUNKWld4d3c0Z245U0p0NlVOTnJDbUJrTnFtQ3ZHMjlWTGkzcFgiLCJzZW5kZXIiOiJSOGdFRXlsSnNvLTBTSV84bExsZDBNS05HNkp2V0R3c3JrcjlMN1JfNXhYU3VrdVFsajk0RkZxU3BremR4dlVxd0RXM0U1NV9yazZBbW1Jb1NqWl90SmFKWWdVVFZ3LTlycXp0VWZ3eTBkcFRMTERNVmloQkVwYU1rMEU9IiwiaXYiOiI5cERsdjV4aWgzcmpzTlExazl2eENuZ0JFc3Y1SmZQVyJ9fV19","iv":"RzVtnhMSALLv5qsa","ciphertext":"2-NivuC-K8SvDH4_empA-fsLR8qNOPpfTNE=","tag":"pIRd32Hm8BCEW_ZYaBz2DA=="}
"""
## END PASTE  ##

print("Using PK: ", b58_pub)
print("Using SK: ", b58_priv)

msg_in = msg_in.encode()

# concat the priv and pub keys to produce the 64-byte nacl priv format
def find_key(param):
	sk = b58_to_bytes(b58_priv)
	return sk

data_in, sender_VK, recip_VK = crypto.decode_pack_message(msg_in, find_key)

print("data in:")

print(data_in)

