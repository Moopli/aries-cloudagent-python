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

b64_pub = "fZVwrHMKi3JynorE5eDi1jHzo-vmIFWQ9dbXfMs57jA="
b64_priv = "q0xM-cokts_2QEqHoaiVZro2NgckC2A-20HbEFs3lnZ9lXCscwqLcnKeisTl4OLWMfOj6-YgVZD11td8yznuMA=="

msg_in = """{"protected":"eyJlbmMiOiJjaGFjaGEyMHBvbHkxMzA1X2lldGYiLCJ0eXAiOiJKV00vMS4wIiwiYWxnIjoiQXV0aGNyeXB0IiwicmVjaXBpZW50cyI6W3siZW5jcnlwdGVkX2tleSI6InF2YlhZQUFyM09pWHN4QVZoWWdNd2NJTUhuVXdCLTk2ZTVNQWE4MlBOd2QybFhtRGEtQzdpMGQwdmZjTHFnRzciLCJoZWFkZXIiOnsia2lkIjoiOVRFOFIyOWRwSEx0c0poaVlGbXJCcmdTTkRpUGJWTmNvOHpIb01CRmhwaGQiLCJzZW5kZXIiOiJTLUFpQUtGeHB4RGZJYVFBREZxdlJkZno2UnZjeGh0amhSczBpWUdpVGhGZFAwdFFuNzNvcGpGelZ4ZnJDVWp5VUVMc1JiLW1VamhFY0ctVU44RXRRSlc1a0hYYTlvWmxVWUtVaG5hM0FZOUtIQmtLSmVqNXFRWmVpTU09IiwiaXYiOiJzTGFBSXRKcllwaGVMa1RydS1vRmZwRTJ4LXhwRnAwVCJ9fV19","iv":"7zNmSKQc3TJ45Pro","ciphertext":"Z9m7zNd6yQ4bkorhZjvVNKmnBhktv1FgsK8=","tag":"DSxJKQ2zgKxbS95RcN1zQg=="}""".encode("ascii")

# concat the priv and pub keys to produce the 64-byte nacl priv format
def find_key(param):
	sk = b64_to_bytes(b64_priv, urlsafe=True)
	return sk

data_in, sender_VK, recip_VK = crypto.decode_pack_message(msg_in, find_key)

print("data in:\n")

print(data_in)

