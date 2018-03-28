#Add all the functions that can be used for cryptopalsself.
import binascii
import collections
from itertools import cycle

#hex to base64 duH!!
def hex_to_base64(hexstring):
    """Covert hex string into base64 string.
    Args:
        hexstring (string): a string represetnation of hex.

    Returns:
        bytes: A bytearray with the base64 result.
    """
    b = bytearray.fromhex(hexstring) #convert str to byte array
    base = binascii.b2a_base64(b) #convert bytearray to base64
    return base


#Send hex string
def xor_repeating_key(d, k):
    """xor a string given a key, if keysize<len(string) repeat the key.
    Args:
        d (bytes): a bytearray of the string to encrpyt/Decrypt.
        k (bytes): a bytearray of the key.

    Returns:
        bytes: A bytearray with the result
    """
    return bytes([d[i] ^ k[i % len(k)] for i in range(len(d))])

#send hex srings
def xor_equallen_key(d, k):
    """xor a string given a key of equal length.
    Args:
        d (bytes): a bytearray of the string to encrpyt/Decrypt.
        k (bytes): a bytearray of the key.

    Returns:
        bytes: A bytearray with the result
    """
    return bytes((''.join(chr(a^b) for a,b in zip(d,k))))


def xor_bruteforce_single(d):
    """bruteforce a ciphertext bytearray using statiscal analysis
    given character frequency histogram. Will attempt range(0,256) as keys

    Args:
        d (bytes): a bytearray of the string to decrypt.

    Returns:
        list: A list with [max_score, max_key, plaintext] with the result
    """
    """
    for key in range(256):
        strings = (''.join(chr(data^key) for data in d))
        c_freq = char_freq(strings)
        score = c_freq
        if score > max_score:
            max_score = score
            max_key = key
            plaintext = strings
    """
    return max([(k, (''.join(chr(data^k) for data in d))) for k in range(0,256)], key=lambda s: char_freq(s[1]))


#calculate how often common characters occur
def char_freq(buf):
    """determine the character frequency within a string

    Args:
        buf (string): a bytearray of the string to decrypt.

    Returns:
        int: the probability of finding english?.
    """
    score = 0
    b = buf.lower() #ease of matching!
    letters = collections.Counter(b)

    for c in letters:
        if   c == 'e': score +=  12.702
        elif c == 't': score +=  9.056
        elif c == 'a': score +=  8.167
        elif c == ' ': score +=  25.000 # added but not statistically accurate
        elif c == 'o': score +=  7.507
        elif c == 'i': score +=  6.966
        elif c == 'n': score +=  6.749
        elif c == 's': score +=  6.327
        elif c == 'h': score +=  6.094
        elif c == 'r': score +=  5.987
        elif c == 'd': score +=  4.253
        elif c == 'l': score +=  4.025
        elif c == 'c': score +=  2.782
        elif c == 'u': score +=  2.758
        elif c == 'm': score +=  2.406
        elif c == 'w': score +=  2.360
        elif c == 'f': score +=  2.228
        elif c == 'g': score +=  2.015
        elif c == 'y': score +=  1.974
        elif c == 'p': score +=  1.929
        elif c == 'b': score +=  1.492
        elif c == 'v': score +=  0.978
        elif c == 'k': score +=  0.772
        elif c == 'j': score +=  0.153
        elif c == 'x': score +=  0.150
        elif c == 'q': score +=  0.095
        elif c == 'z': score +=  0.074

    return score

#Takes two byte arrays
def hamming_distance(x, y):
    return sum([bin(x[i] ^ y[i]).count('1') for i in range(len(x))])
