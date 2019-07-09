def encipher_xor(k1, k2):
	cipher = ""
	k1_len = len(k1)


	for i in range(k1_len):
		cipher += str(k1[i] ^ k2[i])

	return cipher




str1 = b"1c0111001f010100061a024b53535009181c"
str2 = b"686974207468652062756c6c277320657965"

fromhex1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
fromhex2 = bytes.fromhex('686974207468652062756c6c277320657965')

print("str1 = ", str1)
print("str2 = ", str2)
print("1 -> ", fromhex1)
print("2 -> ", fromhex2)

result = ""

for b1, b2 in zip(fromhex1, fromhex2):
	result += chr(b1^b2)

print(result)