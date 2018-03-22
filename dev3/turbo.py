from math import floor, ceil


def bin(n):
    return format(n, 'b')


count = 0


def turbo(a, n):
    global count
    count += 1
    print("turbo(%d, %d)" % (a, n))
    if n == 1:
        return a
    elif n == 2:
        return a * a
    else:
        n_bin = bin(n)
        b = n_bin.count('1')
        if b == 1:
            z = n_bin.count('0')
            p_bin = '1' + ('0' * floor(z/2))
            p = int(p_bin, 2)
            q_bin = '1' + ('0' * ceil(z/2))
            q = int(q_bin, 2)
            return turbo(turbo(a, p), q)
        else:
            p_bin = n_bin[::-1]
            p_bin = p_bin.replace('1', '0', ceil(b / 2))
            p_bin = p_bin[::-1]
            p = int(p_bin, 2)
            return turbo(a, p) * turbo(a, n - p)


print(turbo(2, 51), count)
