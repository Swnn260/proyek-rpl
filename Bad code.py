def h(a, b):
    t = 0
    for i in range(b):
        t = t + a

    if t > 50:
        t = 50

    return t
