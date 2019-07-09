byte1 = [byte for byte in b'this is a test']
byte2 = [byte for byte in b'wokka wokka!!!']

xor_bytes = [b1 ^ b2 for b1,b2 in zip(byte1, byte2)]

print(xor_bytes)

hamming_distance = 0

for byte in xor_bytes:
	hamming_distance += sum([1 for bit in bin(byte) if bit == '1'])

print(hamming_distance)