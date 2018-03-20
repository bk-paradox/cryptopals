#Cyberpals.com challenges

import binascii #Challenge 2 & 3

#Challenge 5
"""
Here is the opening stanza of an important work of the English language:

Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.
"""
from itertools import cycle
def stanza(string):
    key = b"ICE"
    test = list(map(lambda c,k: (c^k), string, cycle(key)))
    ret = binascii.hexlify(bytes(test))
    return str(ret, 'utf-8')


#Challenge 4
"""
Detect single-character XOR
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""
def readfile(file):
    a = []
    f = open(file, 'r')
    for i in f:
        a.append(xorbrute(i.strip()))    
    f.close()
    best = max(a, key=lambda s: sum((26-i) * s.count(c) for i,c in enumerate('eation shrdlu')))
    return best

#Challenge 3
"""
Single-byte XOR cipher
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

Achievement Unlocked
You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
"""
def xorbrute(string):
    nums = binascii.unhexlify(string) #Convert hex to binary-data
    strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
    return max(strings, key=lambda s: s.count(' '))           

#Challenge 2
"""
Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179
"""
def base64hex(string):
    b = bytearray.fromhex(string) #convert str to byte array
    base = binascii.b2a_base64(b) #convert bytearray to base64
    return str(base, 'utf-8') #return base64 string


#Challenge 1
"""
Convert hex to base64
The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

Cryptopals Rule
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
"""

def hexor(string, key):
    r = ''
    d = binascii.unhexlify(string)
    k = binascii.unhexlify(key)
    r = (''.join(chr(a^b) for a,b in zip(d,k))) 
    return r #return hex string


# Challenge 1
chal1 = hexor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") 
print("Challenge 1 : ", chal1)
print("Challenge 1 : ", chal1.encode("utf-8").hex())

# Challenge 2
chal2 = base64hex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") 
print("Challenge 2 : ", str(binascii.a2b_base64(chal2), 'utf-8'))
print("Challenge 2 : ", chal2.strip())

# Challenge 3
print("Challenge 3 : ", xorbrute("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))

# Challenge 4
chal4 = readfile('4.txt') 
print("Challenge 4 : ", chal4.strip())
print("Challenge 4 : ", chal4.encode('utf-8').hex())

#Challenge 5
stazi = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
chal5 = stanza(stazi)
print("Challenge 5 : ", str(stazi, 'utf-8'))
print("Challenge 5 : ", chal5.strip())


