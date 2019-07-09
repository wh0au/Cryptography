
str1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

hex_decoded = bytes.fromhex(str1)
result = ""
count=1
f = open('./ch14txt.txt')

for line in f:
	decoded_line = bytes.fromhex(line)
	for i in range(32,126):
		for ch in decoded_line:
			
			if(((chr(ch ^ i) >= 'a') and (chr(ch ^ i) <= 'z')) or
				(chr(ch ^ i) >= 'A') and (chr(ch ^ i) <= 'Z') or
				(chr(ch ^ i) == ' ')):
				result += chr(ch ^ i)
			else:
				break

		if(len(result) >= 20):
			print("Original string: ", line)
			print("Decoded line: ", decoded_line)
			print("Decrypt_key: ", chr(i))
			print("Line: ", count)
			print("Decrypted Message: ", result)
			
		
		result = ""

	count+=1