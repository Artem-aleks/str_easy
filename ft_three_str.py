def ft_len(a):
    b = 0
    for i in a:
        b += 1

    return b


def ft_three_str(str1, str2, str3):
    # c = str()
    # if str2 in str1:
    #     for i in range(ft_len(str1)):
    #         for j in str2:
    #             if str1[i] == j:
    #                 if str1[i:ft_len(str2) + i] == str2:
    #                     c = str1[:i] + str3 + str1[ft_len(str3) + i:]
    # return c
    return str1.replace(str2, str3)
