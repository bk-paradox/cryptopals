#Comments
#Dont want docstring

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
from itertools import combinations,zip_longest
from binascii import a2b_base64,hexlify
from common import (hamming_distance,xor_bruteforce_single,xor_repeating_key)

def find_xor_keysize(d):
    """Given some ciphertext determine the most likely keysize from 2,42

    Args:
        d (bytes): the cipertext to determine keysize.

    Returns:
        int: the keysize.

    """
    for keysize in range(2,42):
        chunks = [d[i:i+keysize] for i in range(0, len(d), keysize)]
        pairs = list(combinations(chunks, 2))
        distance = [hamming_distance(p[0], p[1]) /float(keysize) for p in pairs]
        return sum(distance) / len(distance)


def break_xor_key(d, k):
    from collections import Counter
    """Note: Given a ciphertext and keysize, break the ciphertext into silos
             The ciphertext will be put into buckets to be bruteforced.
    Args:
        d (bytes): the ciphertext to determine keys
        k (bytes): keysize (predicted)

    Returns:
        bytes: the bytes of the key.
    """
    chunks = [d[i:i+k] for i in range(0, len(d), k)]
    Blocks = list(zip_longest(*chunks, fillvalue=0))
    a = [xor_bruteforce_single(bytes(i))[0] for i in Blocks ]
    return bytes(a)

def main():
    a = b"this is a test"
    b = b"wokka wokka!!!"
    assert(hamming_distance(a, b) == 37) # Test to see if hamming distance is working correctly

    with open("6.txt") as f:
        a = ''.join(f.read().strip().split('\n'))
        ciphertext = a2b_base64(a)

    keysize = find_xor_keysize(ciphertext)
    print("Most likely to be a keysize of : ", int(keysize))
    key = break_xor_key(ciphertext, int(keysize))
    print("Key determined to be : ", key)
    plaintext = xor_repeating_key(ciphertext, key)
    print(plaintext)


if __name__ == '__main__':
    main()
