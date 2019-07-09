def pkcs_pad(data, blocksize=16):
	padval = blocksize - (len(data) % blocksize)
	if padval == 0:
		padval = blocksize
	return data + bytes([padval] * padval)

print(pkcs_pad(b'YELLOW SUBMARINE', 20))