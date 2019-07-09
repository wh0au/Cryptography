#!/usr/bin/env python
'''Fixed XOR'''

def encipher_xor(plain, k):
        cipher = bytearray()
        cipher2 = bytearray()
        for i in xrange(len(plain)):
            cipher2.append(plain[i] ^ k[i])
            cipher.append(chr(plain[i]^k[i%len(k)]))

        print cipher
        return cipher

def main():
    # decode hex encoding to array of bytes 
    barray1 = bytearray('1c0111001f010100061a024b53535009181c'.decode('hex'))
    barray2 = bytearray('686974207468652062756c6c277320657965'.decode('hex'))

    xor = encipher_xor(barray1,barray2)
    print "answer= ", xor 
    print 'xor: {0}'.format(xor)

    # check the answer
    assert(xor == '746865206b696420646f6e277420706c6179'.decode('hex'))

if __name__ == "__main__":
    main()
