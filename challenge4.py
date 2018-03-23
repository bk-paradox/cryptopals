from common import xor_bruteforce_single

def main():
    print("Attempting to find the best, the best of xor!")
    a = [] #list of results
    with open('4.txt') as f:
        for i in f:
            a.append(xor_bruteforce_single(i.strip()))

    best = max(a, key=lambda s: s[0])
    print("Probability score : ", best[0], "\tXor Key : ", best[1], "\nString : ", best[2])

if __name__ == '__main__':
    main()
