
""" Unbreakable Encryption """

# the dummy data must be the same length as the original data, 
# truly random, and completely secret;
#
# our data will not be truly random, in the sense that the secrets package 
# still is using a `pseudo-random number generator` behind the scenes, 
# but it will be close enough for our purposes;

from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
	# generate lenth random bytes
	tb: bytes = token_bytes(length)
	# convert those bytes into a bit string and return it
	return int.from_bytes(tb, "big")

# `XOR` is logical bitwise operation:
# A ^ B = C
# C ^ B = A
# C ^ A = B

def encrypt(original: str) -> Tuple[int, int]:
	original_bytes: bytes = original.encode()
	dummy: int = random_key(len(original_bytes))
	original_key: int = int.from_bytes(original_bytes, "big")
	encrypted: int = original_key ^ dummy	# XOR
	return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
	decrypted: int = key1 ^ key2	# XOR
	temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
	return temp.decode()


if __name__ == "__main__":
	key1, key2 = encrypt("One Time Pad!")
	result: str = decrypt(key1, key2)
	print(result)