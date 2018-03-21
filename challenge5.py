import binascii
from common import xor_repeating_key

def main():
    stanza = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b"ICE"
    encrypted = xor_repeating_key(binascii.hexlify(stanza), binascii.hexlify(key))
    if encrypted == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f":
        print(encrypted)
        print("Successfully encrypted!")

if __name__ == '__main__':
    main()
