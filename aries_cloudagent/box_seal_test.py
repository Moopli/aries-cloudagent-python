#!/usr/bin/env python3

from .wallet import crypto
from .wallet.util import b64_to_bytes
import nacl.bindings

# Paste in b64url data
b64_pub = "cy_nKX-bPHahdPNHGFjhXX0Jm4JepTIPK0e21vYAo30="
b64_priv = "_v_aZ_yl8vbwftKEasInlnBkendrF8wEgklHyOV5UvE="
msg_in = "T8ZNSXLmIdSqHIp8EvS6bXci7tDru_7YoGCOeWJAOtFhnsQgETbMg6sDPgdrjIB13nqmkIfmLbQk1HVm-pPQtm7sXm-B2ac="

pk = b64_to_bytes(b64_pub, urlsafe=True)
sk = b64_to_bytes(b64_priv, urlsafe=True)
msg_in = b64_to_bytes(msg_in, urlsafe=True)

msg_out = nacl.bindings.crypto_box_seal_open(msg_in, pk, sk)

print(msg_out.decode("ascii"))
