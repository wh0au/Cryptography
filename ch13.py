
str1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

hex_decoded = bytes.fromhex(str1)
result = ""
count=1
for i in range(32,126):
	for ch in hex_decoded:
		result += chr(ch ^ i)
	#print("result", count, " = ", result)
	if(count == 57):
		print("result", count, " = ", result)
		print("key = ", chr(i))
	count+=1
	result = ""

