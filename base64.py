import binascii

print("Decoding base64 String")
h = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
b = bytearray.fromhex(h) #convert str to byte array
base = binascii.b2a_base64(b) #convert bytearray to base64
print(str(base, 'utf-8')) #convert binary data to utf-8 encoded str
