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
# print("PK (Ed): ", bytes_to_b58(pkSign))
# print("SK (Ed): ", bytes_to_b58(skSign))

pkSeal = nacl.bindings.crypto_sign_ed25519_pk_to_curve25519(pkSign)
skSeal = nacl.bindings.crypto_sign_ed25519_sk_to_curve25519(skSign)

# print("PK (Curve): ", bytes_to_b58(pkSeal))
# print("SK (Curve): ", bytes_to_b58(skSeal))


# Current recipient keypair used in testcase

## PASTE DATA ##
b58_pub = "AVeG2qbvV33NMCRQzn4Pdq2tvPSSmTywDHD4qiP8oXua"
b58_priv = "2vb73XuT3CZ8w8C1sgDfZxU87JgNt92XYQP72H9UC55aidZmwp5duaAhrKBbMwQrpwQQbKn8TqsWh2cYBGy8ZGsa"
msg_in = """{"protected":"eyJlbmMiOiJjaGFjaGEyMHBvbHkxMzA1X2lldGYiLCJ0eXAiOiJKV00vMS4wIiwiYWxnIjoiQXV0aGNyeXB0IiwicmVjaXBpZW50cyI6W3siZW5jcnlwdGVkX2tleSI6Ik9FbUFZalBYZGZLdXBvR240VlZxTDBDOWZyYWNMdDhXY0hVQ1VVZExSQlJpemVtN3V2cjZaalBvaEtpc3I3WVkiLCJoZWFkZXIiOnsia2lkIjoiQVZlRzJxYnZWMzNOTUNSUXpuNFBkcTJ0dlBTU21UeXdESEQ0cWlQOG9YdWEiLCJzZW5kZXIiOiJRVmJudml1OGZ4UGJyN2VCS0QzbmVXS0RZVC1QMk5KMU5BUHZRMTZCWDFxTlAxbWl2VVAwNG5RNXd3TkhIbnlkZW5MR1QzTTI5YkJaRmRBQ0tXVXRKd0NTSGhSaS10cFlINVBDLVlzTnJvZVA2SDVRb0xzcUI2b1dNMHM9IiwiaXYiOiJHSlVLRk5UQWhoM1lZNVo4MTJrNzdXRkZFdTF6OExxbCJ9fV19","iv":"Wf8D-YaLJoCeIGBk","ciphertext":"rVCYdAcw-htTwQTFvUP-HIaPvm1eoHG8US8=","tag":"lIkWZQZgQ5yDol2Nj1czow=="}
"""
## END PASTE  ##

print("Using PK: ", b58_pub)
print("Using SK: ", b58_priv)

msg_in = msg_in.encode()

# concat the priv and pub keys to produce the 64-byte nacl priv format
def find_key(pub):
	if pub == b58_pub:
		sk = b58_to_bytes(b58_priv)
		return sk
	return None

data_in, sender_VK, recip_VK = crypto.decode_pack_message(msg_in, find_key)

print("data in:")

print(data_in)

