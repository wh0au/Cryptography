import binascii

str1 = "Burning 'em, if you ain't quick and nimble"
str2 = "I go crazy when I hear a cymbal"

#hexed_str1 = binascii.hexlify(str1)
#hexed_str2 = binascii.hexlify(str2)


#now perform xor on each strs
#byte_coutner = 0

encrypt_key = "ICE"
byte_counter = 0
results = ""
for ch in str1:
	
	result = hex(ord(ch) ^ ord(encrypt_key[byte_counter]))
	result = result[2:4]
	#strresult == result.encode("utf-8").hex()
	results += str(result)
	
	print("XOR: ", ch, " ", encrypt_key[byte_counter], "----> ", result)
	

	if(byte_counter == 2):
		byte_counter = 0
	else:
		byte_counter += 1
print(results)
#print(binascii.hexlify(result))
