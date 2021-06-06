import string, sys

def encrypt(k, m):
    # upper(): 将字符串中的小写字母转为大写字母。
    # ord(): 返回对应的 ASCII 数值，或者 Unicode 数值。一般与chr()配对使用
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
        # 从用户的输入中获取参数
        k = sys.argv[1]
        m = sys.argv[2]
    except:
        k = input("Key:")
        m = input("Plaintext:")
        c = encrypt(k, m)
        print(' '.join(c[i:i+5] for i in range(0, len(c), 5)))

