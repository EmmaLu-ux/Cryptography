
import string, sys

def decrypt(k, c):
    shift = ord(k.upper()) - 65
    m = ""
    for m1 in (c.replace(' ',"")).lower():
        print("ciphertext:",m1)
        nchr = chr(ord(m1) - shift)
        if ord(nchr) < 97:
            nchr = chr(ord(nchr) + 26)
        elif ord(nchr) > 122:
            nchr = chr(ord(nchr) + 26)
        else:
            m += nchr
    return m

if __name__ == '__main__':
    try:
        k = sys.argv[1]
        c = sys.argv[2]
    except:
        k = input("Key:")
        c = input("Ciphertext:")
        m = decrypt(k, c)
        print("Plaintext:", m)























