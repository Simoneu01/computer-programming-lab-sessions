def capi(s):
    tmp = s[0]
    if ord(tmp) >= 97 and ord(tmp) < 123:
        tmp = chr(ord(tmp) - 32)
    else:
        tmp = s[0]
    return tmp + s[1:]

with open('lorem.txt', 'r') as f:
    uppercase = []
    lines = f.readlines()
    for line in lines:
        upperc = [capi(i) for i in line.split()]
        uppercase.append(' '.join(upperc) + '\n')

with open('uppercase.txt', 'w') as f:
    print(uppercase)
    f.writelines(uppercase)
