from common import hex_to_base64

def main():
    print("Decoding base64 String")
    h = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(str(hex_to_base64(h), 'utf-8')) #convert binary data to utf-8 encoded str

if __name__ == '__main__':
	main()
