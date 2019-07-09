from Crypto.Cipher import AES
import base64
key = 'YELLOW SUBMARINE'

encipher = AES.new(key, AES.MODE_ECB)

with open('ch17txt.txt') as fh:
	ciphertext = base64.b64decode(fh.read())

print("======================")
print(encipher.encrypt(ciphertext))