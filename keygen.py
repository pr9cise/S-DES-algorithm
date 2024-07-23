def keygenfunct(keytext):
    #key convertion
    keyint = int(keytext)
    key10 = bin(keyint)[2:]
    fullkey = ""
    if len(key10) < 10:
        m = 10-len(key10)
        n = ""
        for i in range (m):
            n += "0"
        n += key10
        fullkey = n
    else:
        fullkey = key10
    print(fullkey)
    #P10 premutation
    p10key = ""
    p10key += fullkey[2] + fullkey[4] + fullkey[1] + fullkey[6] + fullkey[3] + fullkey[9] + fullkey[0] + fullkey[8] + fullkey[7] + fullkey[5]
    print(p10key)
    #first division
    l1 = ""
    r1 = ""
    l1 += p10key[0] + p10key[1] + p10key[2] + p10key[3] + p10key[4]
    r1 += p10key[5] + p10key[6] + p10key[7] + p10key[8] + p10key[9]
    print(f"{l1}\t{r1}")
    #one bit left-shift
    n = 1
    shiftedl1 = l1[n:] + l1[:n]
    shiftedr1 = r1[n:] + r1[:n]
    print(f"{shiftedl1}\t{shiftedr1}")
    #P8 premutation + key1
    combinedkey1 = shiftedl1 + shiftedr1
    p8key1 = ""
    p8key1 += combinedkey1[5] + combinedkey1[2] + combinedkey1[6] + combinedkey1[3] + combinedkey1[7] + combinedkey1[4] + combinedkey1[9] + combinedkey1[8]
    print(f"Key 1 is : {p8key1}")
    #two bit left-shift
    n = 2
    shiftedl2 = shiftedl1[n:] + shiftedl1[:n]
    shiftedr2 = shiftedr1[n:] + shiftedr1[:n]
    print(f"{shiftedl2}\t{shiftedr2}")
    #P8 premutation + key2
    combinedkey2 = shiftedl2 + shiftedr2
    p8key2 = ""
    p8key2 += combinedkey2[5] + combinedkey2[2] + combinedkey2[6] + combinedkey2[3] + combinedkey2[7] + combinedkey2[4] + combinedkey2[9] + combinedkey2[8]
    print(f"Key 2 is : {p8key2}")
    return p8key1, p8key2
"""
text = 642
a = ""
b = ""
a, b = keygenfunct(text)
print(f"Keys\n{a}\n{b}")
"""
