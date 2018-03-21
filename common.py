#Add all the functions that can be used for cryptopalsself.
import binascii
import collections
from itertools import cycle

#hex to base64 duH!!
def hex_to_base64(hexstring):
    b = bytearray.fromhex(hexstring) #convert str to byte array
    base = binascii.b2a_base64(b) #convert bytearray to base64
    return base


#Send hex string
def xor_repeating_key(string, key):
    d = binascii.unhexlify(string)
    k = binascii.unhexlify(key)
    test = list(map(lambda c,z: (c^z), d, cycle(k)))
    ret = binascii.hexlify(bytes(test))
    return str(ret, 'utf-8')

#send hex srings
def xor_equallen_key(string, key):
    r = ''
    d = binascii.unhexlify(string)
    k = binascii.unhexlify(key)
    r = (''.join(chr(a^b) for a,b in zip(d,k)))
    return r #return hex string

#send hex string
def xor_bruteforce_single(string):
    d = binascii.unhexlify(string)
    plaintext = ''
    max_score = 0
    key = ''
    for key in range(256):
        strings = (''.join(chr(data^key) for data in d))
        c_freq = char_freq(strings)
        score = c_freq
        if score > max_score:
            max_score = score
            max_key = key
            plaintext = strings
    return (max_score, max_key, plaintext)


#calculate how often common characters occur
def char_freq(buf):
	score = 0
	b = buf.lower() #ease of matching!
	letters = collections.Counter(b)

	for c in letters:
		if   c == 'e': score += letters['e'] * 12.702
		elif c == 't': score += letters['t'] * 9.056
		elif c == 'a': score += letters['a'] * 8.167
		elif c == ' ': score += letters[' '] * 8.000 # added but not statistically accurate
		elif c == 'o': score += letters['o'] * 7.507
		elif c == 'i': score += letters['i'] * 6.966
		elif c == 'n': score += letters['n'] * 6.749
		elif c == 's': score += letters['s'] * 6.327
		elif c == 'h': score += letters['h'] * 6.094
		elif c == 'r': score += letters['r'] * 5.987
		elif c == 'd': score += letters['d'] * 4.253
		elif c == 'l': score += letters['l'] * 4.025
		elif c == 'c': score += letters['c'] * 2.782
		elif c == 'u': score += letters['u'] * 2.758
		elif c == 'm': score += letters['m'] * 2.406
		elif c == 'w': score += letters['w'] * 2.360
		elif c == 'f': score += letters['f'] * 2.228
		elif c == 'g': score += letters['g'] * 2.015
		elif c == 'y': score += letters['y'] * 1.974
		elif c == 'p': score += letters['p'] * 1.929
		elif c == 'b': score += letters['b'] * 1.492
		elif c == 'v': score += letters['v'] * 0.978
		elif c == 'k': score += letters['k'] * 0.772
		elif c == 'j': score += letters['j'] * 0.153
		elif c == 'x': score += letters['x'] * 0.150
		elif c == 'q': score += letters['q'] * 0.095
		elif c == 'z': score += letters['z'] * 0.074

	return score

#Takes two byte arrays
def hamming_distance(s1, s2):
    a = bin(int(binascii.hexlify(s1),16))
    b = bin(int(binascii.hexlify(s2),16))
    #Compare all mistmatches between corespondng postions in the two inputs
    #summing the sequence with false and true values being interpreted as zero and one
    return sum(el1 != el2 for el1,el2 in zip(a,b))
