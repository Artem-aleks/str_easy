def ft_len(a):
    b = 0
    for i in a:
        b += 1

    return b


def ft_slice_str(string, start, stop):
    v = ''
    for i in range(start, stop):
        v += string[i]
    return v
