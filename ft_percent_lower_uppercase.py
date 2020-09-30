UPPERCASE = 'QWERTYUIOPASDFGHJKLZXCVBNMЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
LOWERCASE = 'qwertyuiopasdfghjklzxcvbnmёйцукенгшщзхъфывапролджэячсмитьбю'


def ft_percent_lower_uppercase(a):
    b = 0
    c = 0
    for char in a:
        if char in UPPERCASE:
            b += 1
        elif char in LOWERCASE:
            c += 1
    return b / c * 100
