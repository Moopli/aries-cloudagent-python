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

b64_pub = "SFwkxB6OHiJgGh3wWd_4ZLq2-XcosiNjGhK84Yg3Jyg="
b64_priv = "sIHSXY9ANBOyqWXmFvmXzOTTZlEW2EtKUkWcT6xXo4g="

msg_in = """{"protected":"eyJlbmMiOiJjaGFjaGEyMHBvbHkxMzA1X2lldGYiLCJ0eXAiOiJKV00vMS4wIiwiYWxnIjoiQXV0aGNyeXB0IiwicmVjaXBpZW50cyI6W3siZW5jcnlwdGVkX2tleSI6IjNWcWgyaWRJZm1nYVQ3LUs2QUNPak5qMm41NF9FYkpicnRSQkN1U2pPN2VILXVEa2FhR054d0l1NjdvdHFwTDgiLCJoZWFkZXIiOnsia2lkIjoiNXNUcjZoVGVENWhIcXZCZ0JFaUtweFpFU3JRbnVXOUNSSmZ6YTczbUF3RXciLCJzZW5kZXIiOiJXcGtaMmhOT2ktekQyamlwZzFkREM3QzVqVzE0UGF4QTdKVUw3UmRaWHpkSS1iZnI3R2cycnNwRlVrd0xQNWRpWXc0V2U0bzBYWmdPS1pZdHlGSkxldmhueVNmN0E2MWFrU2c2dHZnQVN2MWxQV3ZwRWRXQ3lUSHE5UE09IiwiaXYiOiJVUV94TXhuU0dDN19zbTJLYndvRGNCUEU5OElrbzNlaCJ9fV19","iv":"ONbsFv3XBKJm7zsH","ciphertext":"JTcCktit29m9MCg4-w4XyyhnKCZ_JfpgrQ0=","tag":"Q2xVeiyFi9j1F5wuL0Fixg=="}""".encode("ascii")

# concat the priv and pub keys to produce the 64-byte nacl priv format
def find_key(param):
	sk = b64_to_bytes(b64_priv, urlsafe=True)
	pk = b64_to_bytes(b64_pub, urlsafe=True)
	return sk + pk

data_in, sender_VK, recip_VK = crypto.decode_pack_message(msg_in, find_key)

print("data in:\n")

print(data_in)

