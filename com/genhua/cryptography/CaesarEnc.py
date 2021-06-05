import string, sys

def encrypt(k, m):
    shift = ord(k.upper()) - 65
    c = ""
    for c1 in (m.replace(' ',"")).upper():
        print("plaintext:",c1)
        nchr = chr(ord(c1) + shift)
        if ord(nchr) > 90:
            nchr = chr(ord(c1) - 26)
        c += nchr
    return c

if __name__ == '__main__':
    try:
        k = sys.argv[1]
        m = sys.argv[2]
    except:
        k = input("Key:")
        m = input("Plaintext:")
        c = encrypt(k, m)
        print(' '.join(c[i:i+5] for i in range(0, len(c), 5)))






















