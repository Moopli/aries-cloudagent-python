#!/usr/bin/env python3

from .wallet import crypto
from .wallet.util import b64_to_bytes
import nacl.bindings

def make_seed(data: bytes):
	seed = bytearray(nacl.bindings.crypto_sign_SEEDBYTES)
	seed[:len(data)] = data[:len(seed)]
	seed = bytes(seed)
	# print(len(seed) - nacl.bindings.crypto_sign_SEEDBYTES)
	return seed

b64_priv = "Vo5QC9Zu63xXoGUpsUkp2jqMb82NpoXeYCjAL6-8-h0="
b64_pub = "uYe6j0Qev6NzeXRVmaAAOjObSSKZ4FVWY8Zd8kTUUeg="

msg_in = """{"protected": "eyJlbmMiOiJjaGFjaGEyMHBvbHkxMzA1X2lldGYiLCJ0eXAiOiJKV00vMS4wIiwiYWxnIjoiQXV0aGNyeXB0IiwicmVjaXBpZW50cyI6W3siZW5jcnlwdGVkX2tleSI6ImlIdVhaLWF2S1dPN3A2a3R4UUZtR2Z2YXhrVkRvZnZHaG9QaVlOTlRPOThJVHBnbG54V2RMcnBEdkZCU2lsdWciLCJoZWFkZXIiOnsia2lkIjoiNnBzdmJZdWNyaTFXS2VSczl4NmpjM3hQMjVCMjVNNDZaVmU4ZmJMZHI1VWciLCJzZW5kZXIiOiJlekhkUGZfZUdGVjhTOXcwNl8zTXFxZ093NTV4V0R5R3JsVFBZQ3d5YW1SRVVVaE0tRmRIWjRLdkFsMWhnd0ZVOEVUemFMQklvb0F2RXRReXdEaEJ5ZzktLUpYRmZKX1V5TENxbnBvdHZPT2o3bDQ4YjBSY3NuMk5DRXM9IiwiaXYiOiJHeE42amhiX0dpNTNZZ1NzWHptVV9LQ3FxNi1UV2NxZSJ9fV19","iv": "suRbgrIHnQbwdZw8","ciphertext": "5EO8owxaZZNXlF3p73fHUeq4FKlLylQJTDk=","tag": "5tKgm201H5cZeQfzuR6TBQ=="}""".encode("ascii")

# concat the priv and pub keys to produce the 64-byte nacl priv format
def find_key(param):
	sk = b64_to_bytes(b64_priv, urlsafe=True)
	pk = b64_to_bytes(b64_pub, urlsafe=True)
	return sk + pk

print("key: ", find_key(b64_priv))

data_in, sender_VK, recip_VK = crypto.decode_pack_message(msg_in, find_key)

print("data in:\n")

print(data_in)

