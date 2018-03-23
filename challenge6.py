#Comments
#Dont want docstring
from binascii import a2b_base64,hexlify
from common import (hamming_distance,xor_bruteforce_single)
"""
https://cryptopals.com/sets/1/challenges/6
Break repeating-key XOR
It is officially on, now.
This challenge isn't conceptually hard, but it involves actual error-prone coding.
The other challenges in this set are there to bring you up to speed. This one is there to qualify you. If you can do this one, you're probably just fine up to Set 6.

There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
Write a function to compute the edit distance/Hamming distance between two strings.
The Hamming distance is just the number of differing bits. The distance between:
this is a test
and
wokka wokka!!!
is 37. Make sure your code agrees before you proceed.
For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes,
and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
The KEYSIZE with the smallest normalized edit distance is probably the key.
You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
Now transpose the blocks: make a block that is the first byte of every block,
and a block that is the second byte of every block, and so on.
Solve each block as if it was single-character XOR. You already have code to do this.
For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block.
Put them together and you have the key.
This code is going to turn out to be surprisingly useful later on.
Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise,
 a "Crypto 101" thing. But more people "know how" to break it than can actually break it,
  and a similar technique breaks something much more important.

No, that's not a mistake.
We get more tech support questions for this challenge than any of the other ones. We promise, there aren't any blatant errors in this text. In particular: the "wokka wokka!!!" edit distance really is 37.
"""


#To get an accurate difference we go to the binary level
a = b"this is a test"
b = b"wokka wokka!!!"
assert(hamming_distance(a, b) == 37) # Test to see if hamming distance is working correctly

with open("6.txt") as f:
    a = ''.join(f.read().strip().split('\n'))
    ciphertext = a2b_base64(a)
ham = []

for keysize in range(2,40):
    chunks = []
    for i in range(0, len(ciphertext), keysize):
        #Create keysize chunks to measure the distance
        chunks.append(ciphertext[i:keysize + i])

    distances = []
    for i in range(0, 8, 2): #Take the first 4 samples
        distances.append(hamming_distance(chunks[i], chunks[i+1]) / keysize)
    """
    for z in range(0,len(chunks)):
        for y in range(1,len(chunks)):
            distances.append((hamming_distance(chunks[z], chunks[y]) / keysize))
    """
#Average the hamming distance for chunks of the current keysize.
    average_distance = sum(distances) / len(distances)
    ham.append((average_distance,keysize))
    # print("Keysize : ", keysize, "\tNormalized ham : ", average_distance)
#sort based on lowest hamming score.
sorted(ham, key=lambda s: s[0])

#choose the first keysize
keysize = ham[0][1]
print("Most likely to be a keysize of : ", keysize)
#Need to now take the first byte of each key and do a xor bruteforce
#transpose the block, make a block that is the first byte of every block,
#and a block that is the second byte of every block, and so on.

cha = []
#create a list of lists to cover a byte array for each byte within the chunk
for i in range(keysize):
    cha.append([])

#Break the ciphertext out into their respective lists
for a in range(len(ciphertext)):
    #go through ciphertext assigning bytes to respective byte arrays
    #may be a more efficent way to do this!!
    cha[a % keysize].append(ciphertext[a])

#Implement combining the two keys to attempt xor_repeating_key with possibility.
test = xor_bruteforce_single(hexlify(bytes(cha[0])))
print(test)
