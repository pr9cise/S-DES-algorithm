import keygen
def encryptionfunction():
    S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
    key1 = ""
    key2 = ""
    text = input("Введіть текст:\n")
    hexencryptedtext = ""
    asciiencryptedtext = ""
    key = input("Введіть ключ: ")
    key1, key2 = keygen.keygenfunct(key)
    print(f"{key1}\n{key2}")
    for i in range (len(text)):
        #creating 8-bit sequence from letter
        symbol = text[i]
        print(ord(symbol))
        bit = bin(ord(symbol))
        print(bit)
        clearbit = bit[2:]
        fullbit = ""
        if len(clearbit) < 8:
            m = 8-len(clearbit)
            n = ""
            for i in range (m):
                n += "0"
            n += clearbit
            fullbit = n
        else:
            fullbit = clearbit
        print(f"fullbit = {fullbit}")
        #We perform initial permutation on our 8-bit plain text using the IP table.
        IP8bit = ""
        IP8bit += fullbit[1] + fullbit[5] + fullbit[2] + fullbit[0] + fullbit[3] + fullbit[7] + fullbit[4] + fullbit[6]
        print(IP8bit)
        #After the initial permutation, we get an 8-bit block of text which we divide into 2 halves of 4 bit each
        l1 = IP8bit[:4]
        r1 = IP8bit[4:]
        print(f"l1 = {l1}\tr1 = {r1}")
        #On the right half, we perform expanded permutation using EP table which converts 4 bits into 8 bits.
        EP1bit = ""
        EP1bit += r1[3] + r1[0] + r1[1] + r1[2] + r1[1] + r1[2] + r1[3] + r1[0]
        print(EP1bit)
        #We perform XOR operation using the first key K1 with the output of expanded permutation
        int_key1 = int(key1, 2)
        int_EP1bit = int(EP1bit, 2)
        xor_result = int_key1 ^ int_EP1bit
        XOR_EP1bit_key1 = bin(xor_result)[2:]
        full_XOR_EP1bit_key1 = ""
        if len(XOR_EP1bit_key1) < 8:
            m = 8-len(XOR_EP1bit_key1)
            n = ""
            for i in range (m):
                n += "0"
            n += XOR_EP1bit_key1
            full_XOR_EP1bit_key1 = n
        else:
            full_XOR_EP1bit_key1 = XOR_EP1bit_key1
        print(full_XOR_EP1bit_key1)
        #Again we divide the output of XOR into 2 halves of 4 bit each
        l2 = full_XOR_EP1bit_key1[:4]
        r2 = full_XOR_EP1bit_key1[4:]
        print(f"l2 = {l2}\tr2 = {r2}")
        #We take the first and fourth bit as row and the second and third bit as a column for our S boxes
        row_first_S0 = ""
        column_first_S0 = ""
        row_first_S1 = ""
        column_first_S1 = ""
        row_first_S0 += l2[0] + l2[3]
        column_first_S0 += l2[1] + l2[2]
        print(f"S0 = {row_first_S0}\t{column_first_S0}")
        row_first_S1 += r2[0] + r2[3]
        column_first_S1 += r2[1] + r2[2]
        print(f"S1 = {row_first_S1}\t{column_first_S1}")
        first_S0_result = S0[int(row_first_S0, 2)][int(column_first_S0, 2)]
        first_S1_result = S1[int(row_first_S1, 2)][int(column_first_S1, 2)]
        print(f"S0\t{[int(row_first_S0, 2)]}\t{[int(column_first_S0, 2)]}")
        print(f"S1\t{[int(row_first_S1, 2)]}\t{[int(column_first_S1, 2)]}")
        print(first_S0_result)
        print(first_S1_result)
        if len(bin(first_S0_result)[2:]) < 2:
            first_S0_result = "0" + bin(first_S0_result)[2:]
        else:
            first_S0_result = bin(first_S0_result)[2:]
        if len(bin(first_S1_result)[2:]) < 2:
            first_S1_result = "0" + bin(first_S1_result)[2:]
        else:
            first_S1_result = bin(first_S1_result)[2:]
        first_Sbox_result = first_S0_result + first_S1_result
        print(first_S0_result)
        print(first_S1_result)
        print(first_Sbox_result)
        #S boxes gives a 2-bit output which we combine to get 4 bits and then perform permutation using the P4 table.
        Sbox_P4 = ""
        Sbox_P4 += first_Sbox_result[1] + first_Sbox_result[3] + first_Sbox_result[2] + first_Sbox_result[0]
        #We XOR the output of the P4 table with the left half of the initial permutation table i.e. IP table.
        xor_result = int(Sbox_P4, 2) ^ int(l1, 2)
        XOR_P4_l1 = ""
        if len(bin(xor_result)[2:]) < 4:
            m = 4 - len(bin(xor_result)[2:])
            n = ""
            for i in range (m):
                n += "0"
            n += bin(xor_result)[2:]
            XOR_P4_l1 = n
        else:
            XOR_P4_l1 = bin(xor_result)[2:]
        print(XOR_P4_l1)
        #We combine both halves i.e. right half of initial permutation and output of ip.
        #Now, divide the output into two halves of 4 bit each. Combine them again, but now the left part should become right and the right part should become left.
        combined = r1 + XOR_P4_l1
        print(combined)
        #Again perform step 2, but this time while doing XOR operation after expanded permutation use key 2 instead of key 1.
        print("//////////////////2 step//////////////////")
        l3 = combined[:4]
        r3 = combined[4:]
        print(f"l3 = {l3}\tr3 = {r3}")
        #On the right half, we perform expanded permutation using EP table which converts 4 bits into 8 bits.
        EP2bit = ""
        EP2bit += r3[3] + r3[0] + r3[1] + r3[2] + r3[1] + r3[2] + r3[3] + r3[0]
        print(EP2bit)
        #We perform XOR operation using the second key K2 with the output of expanded permutation
        int_key2 = int(key2, 2)
        int_EP2bit = int(EP2bit, 2)
        xor_result = int_key2 ^ int_EP2bit
        XOR_EP2bit_key2 = bin(xor_result)[2:]
        full_XOR_EP2bit_key2 = ""
        if len(XOR_EP2bit_key2) < 8:
            m = 8-len(XOR_EP2bit_key2)
            n = ""
            for i in range (m):
                n += "0"
            n += XOR_EP2bit_key2
            full_XOR_EP2bit_key2 = n
        else:
            full_XOR_EP2bit_key2 = XOR_EP2bit_key2
        print(full_XOR_EP2bit_key2)
        #Again we divide the output of XOR into 2 halves of 4 bit each.
        l4 = full_XOR_EP2bit_key2[:4]
        r4 = full_XOR_EP2bit_key2[4:]
        #We take the first and fourth bit as row and the second and third bit as a column for our S boxes.
        row_second_S0 = ""
        column_second_S0 = ""
        row_second_S1 = ""
        column_second_S1 = ""
        row_second_S0 += l4[0] + l4[3]
        column_second_S0 += l4[1] + l4[2]
        print(f"S0 = {row_second_S0}\t{column_second_S0}")
        row_second_S1 += r4[0] + r4[3]
        column_second_S1 += r4[1] + r4[2]
        print(f"S1 = {row_second_S1}\t{column_second_S1}")
        second_S0_result = S0[int(row_second_S0, 2)][int(column_second_S0, 2)]
        second_S1_result = S1[int(row_second_S1, 2)][int(column_second_S1, 2)]
        print(f"S0\t{[int(row_second_S0, 2)]}\t{[int(column_second_S0, 2)]}")
        print(f"S1\t{[int(row_second_S1, 2)]}\t{[int(column_second_S1, 2)]}")
        print(second_S0_result)
        print(second_S1_result)
        if len(bin(second_S0_result)[2:]) < 2:
            second_S0_result = "0" + bin(second_S0_result)[2:]
        else:
            second_S0_result = bin(second_S0_result)[2:]
        if len(bin(second_S1_result)[2:]) < 2:
            second_S1_result = "0" + bin(second_S1_result)[2:]
        else:
            second_S1_result = bin(second_S1_result)[2:]
        second_Sbox_result = second_S0_result + second_S1_result
        print(second_S0_result)
        print(second_S1_result)
        print(second_Sbox_result)
        #S boxes gives a 2-bit output which we combine to get 4 bits and then perform permutation using the P4 table.
        second_Sbox_P4 = ""
        second_Sbox_P4 += second_Sbox_result[1] + second_Sbox_result[3] + second_Sbox_result[2] + second_Sbox_result[0]
        #We XOR the output of the P4 table with the left half of the initial permutation table i.e. IP table.
        xor2_result = int(second_Sbox_P4, 2) ^ int(l3, 2)
        XOR2_P4_l3 = ""
        if len(bin(xor2_result)[2:]) < 4:
            m = 4 - len(bin(xor2_result)[2:])
            n = ""
            for i in range(m):
                n += "0"
            n += bin(xor2_result)[2:]
            XOR2_P4_l3 = n
        else:
            XOR2_P4_l3 = bin(xor2_result)[2:]
        print(XOR2_P4_l3)
        #We combine both halves i.e. right half of initial permutation and output of ip.
        combined2 = XOR2_P4_l3 + r3
        print(combined2)
        #Perform inverse initial permutation. The output of this table is the cipher text of 8 bit.
        outputtext = ""
        outputtext += combined2[3] + combined2[0] + combined2[2] + combined2[4] + combined2[6] + combined2[1] + combined2[7] + combined2[5]
        print(outputtext)
        #converting text from binary to hex
        hexoutputtext = hex(int(outputtext, 2))[2:]
        fullhex = ""
        if len(hexoutputtext) < 2:
            m = 2 - len(hexoutputtext)
            n = ""
            for i in range(m):
                n += "0"
            n += hexoutputtext
            fullhex = n
        else:
            fullhex = hexoutputtext
        print(fullhex)
        hexencryptedtext += fullhex + " "
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(f"your text\n{hexencryptedtext}")