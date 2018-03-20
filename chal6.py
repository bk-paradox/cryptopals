#Comments
"""
https://cryptopals.com/sets/1/challenges/6
Break repeating-key XOR
It is officially on, now.
This challenge isn't conceptually hard, but it involves actual error-prone coding. The other challenges in this set are there to bring you up to speed. This one is there to qualify you. If you can do this one, you're probably just fine up to Set 6.

There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:
this is a test
and
wokka wokka!!!
is 37. Make sure your code agrees before you proceed.
For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
Solve each block as if it was single-character XOR. You already have code to do this.
For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.
This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.

No, that's not a mistake.
We get more tech support questions for this challenge than any of the other ones. We promise, there aren't any blatant errors in this text. In particular: the "wokka wokka!!!" edit distance really is 37.
"""

import binascii

def xorbrute(string):
    nums = binascii.unhexlify(string) #Convert hex to binary-data
    strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
    return max(strings, key=lambda s: sum((26-i) * s.count(c) for i,c in enumerate('eation shrdlu')))

def hamming_distance(s1, s2):
    a = bin(int(binascii.hexlify(s1),16))
    b = bin(int(binascii.hexlify(s2),16))
    #Compare all mistmatches between corespondng postions in the two inputs
    #summing the sequence with false and true values being interpreted as zero and one
    return sum(el1 != el2 for el1,el2 in zip(a,b))

#To get an accurate difference we go to the binary level
a = b"this is a test"
b = b"wokka wokka!!!"
print(hamming_distance(a, b))

f = open("6.txt")
a = ''.join(f.read().strip().split('\n'))
ciphertext = binascii.a2b_base64(a)
ham = []

for keysize in range(2,40):
    chunks = []
    print("Finding hamming distance for keysize : ", keysize)
    for i in range(0, len(ciphertext), keysize):
        #Create keysize chunks to measure the distance
        chunks.append(ciphertext[i:keysize + i])

    distances = []
    for z in range(0,len(chunks)):
        for y in range(1,len(chunks)):
            distances.append((hamming_distance(chunks[z], chunks[y]) / keysize))
#Average the hamming distance for chunks of the current keysize.
    average_distance = sum(distances) / len(distances)
    ham.append((average_distance,keysize))
    print("Keysize : ", keysize, "\tNormalized ham : ", average_distance)
#sort based on lowest hamming score.
sorted(ham, key=lambda s: s[0])

#choose the first keysize
keysize = ham[0][1]


cha = []
for i in range(keysize):
    cha.append([])
for i in range(len(ciphertext)):
    cha[i % keysize].append(ciphertext[i])
xorbrute(cha)
print(cha)
