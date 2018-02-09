p = (15, 10, 60)
c = (25, 20, 10)
d = (5, 12, 2)


def horaire(n):
    h = list(range(n))
    h.sort(key=lambda i: p[i] + c[i] + d[i], reverse=True)
    return h


def calc_time(h):
    wait = 0
    times = []
    for i in h:
        t = wait + p[i] + c[i] + d[i]
        times.append(t)
        wait += p[i]
    return times


h = horaire(3)
times = calc_time(h)
total = max(times)

print('horaire', h)
print('times', times)
print('total', total)
