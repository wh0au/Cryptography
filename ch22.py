from Crypto.Cipher import AES
import base64

def pad(data, blocksize=16):
	padval = blocksize - (len(data) % blocksize)
	if padval == 0:
		padval = blocksize
	return data + bytes([padval] * padval)

#print(pkcs_pad(b'YELLOW SUBMARINE', 20))

def bxor(b1, b2):
    result = bytearray(b1)
    for i, b in enumerate(b2):
        result[i] ^= b
    return bytes(result)

def cbc_encrypt():

	print("")
	print("=======================")
	print("ENCRYPTING CBC")
	print("=======================")
	print("")

	key = 'YELLOW SUBMARINE'
	iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
	
	encipher = AES.new(key, AES.MODE_ECB)
	#iv length = 16 bytes
	

	block = 16

	plain = 'YELLOW SUBMARINE'

	plain_len = len(plain)


	bplain = bytes(plain, 'utf-8')	

	prev_block = iv

	result = b''

	for i in range(0, plain_len):
		index = 16 * i

		if((plain_len - index) == 0):
			break


		elif((plain_len - index) < 16):
			curblock = pad(bplain[index:], 16)

			print("Current plain block is : ", curblock)
			print("XOR-ing with : ", prev_block)

			xored = bxor(prev_cipher, curblock)
			
			print("XOR-ed : ", xored)

			cur_cihper = encipher.encrypt(xored)

			print("Current Cipher block: ", cur_cipher)
			print("")


			result += cur_cihper
			#print(result)

			break

		else:

			curblock = bplain[index:index+16]
			
			print("Current plain block is : ", curblock)
			

			#print(curblock)
			if(i == 0):
				print("XOR-ing with IV : ", prev_block)
				xored = bxor(iv, curblock)
			else:
				print("XOR-ing with : ", prev_block)
				xored = bxor(prev_cipher, curblock)
			
			print("XOR-ed : ", xored)	

			cur_cipher = encipher.encrypt(xored)

			print("Current Cipher block: ", cur_cipher)
			print("")

			result += cur_cipher
			prev_cipher = cur_cipher

	print("CBC RESULT : ", result)
	print("RESULT LEN: ", len(result))
	return result

def cbc_decrypt(result):
	print("")
	print("=======================")
	print("DECRYPTING CBC")
	print("=======================")
	print("")


	key = 'YELLOW SUBMARINE'
	iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

	decipher = AES.new(key, AES.MODE_ECB)


	result_len = len(result)

	decrypted = b''

	for i in range(0, result_len):
		index = 16 * i

		if((result_len - index) == 0):
			break


		elif((result_len - index) < 16):

			print("Current cipher block is : ", cur_cipher)

			cur_decipher = decipher.decrypt(result[index:])

			print("Deciphered current cipher: ", cur_decipher)

			print("XOR-ing with : ", prev_cipher)

			plain = bxor(prev_cipher, cur_decipher)
			
			print("Current Plain Block : ", plain)


			decrypted += bytes(plain)

			break

		else:

			cur_cipher = result[index:index+16]
			
			print("Current cipher block is : ", cur_cipher)
			
			cur_decipher = decipher.decrypt(cur_cipher)

			print("Deciphered block : ", cur_decipher)

			#print(curblock)
			if(i == 0):
				print("Xor-ing with IV : ", iv)
				plain = bxor(iv, cur_decipher)
			else:
				print("XOR-ing with : ", prev_cipher)
				plain = bxor(prev_cipher, cur_decipher)
			
			print("Current Plain Block : ", plain)	

			print("")

			decrypted += bytes(plain)
			prev_cipher = cur_cipher

	print("Decrypted Result : ", decrypted)


def main():
	result = cbc_encrypt()

	cbc_decrypt(result)



	f = open("ch22txt.txt", "r")
	fdata = f.read()

	print("")
	print("=======================")
	print("DECRYPTING FILE")
	print("=======================")
	print("")

	fdata = base64.b64decode(fdata+"=")

	cbc_decrypt(fdata)

if __name__ == '__main__':
    main()






















