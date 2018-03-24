from common import xor_bruteforce_single
from binascii import unhexlify

def main():
    print("Attempting to find the best, the best of xor!")
    a = [] #list of results
    with open('4.txt') as f:
        for i in f:
            a.append(xor_bruteforce_single(unhexlify(i.strip())))

    best = max(a, key=lambda s: s[0])
    print("Xor Key : ", best[0], "\nString : ", best[1])

if __name__ == '__main__':
    main()
