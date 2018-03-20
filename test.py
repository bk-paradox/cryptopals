import binascii
string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
nums = binascii.unhexlify(string) #Convert hex to binary-data
strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
test = max(strings, key=lambda s: sum((26-i) * s.count(c) for i, c in enumerate('etaoinshrdlu')))
print(keyparty, " : ", test)

