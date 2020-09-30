def ft_cmp_str(str1, str2, num):
    b = str()
    b += str1[:num] + str2 + str1[num:]
    return b
