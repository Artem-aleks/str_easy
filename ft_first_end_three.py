def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return b


def ft_first_end_three(a):
    v = ft_len(a)
    n = 3
    if v > 5:
        for i in range(v):
            if i <= 2 or i >= v - n:
                print(a[i])
    else:
        for c in range(v):
            print(a[0])
