def xor(a, b):
    return (a and not b) or (not a and b)


print(xor([1, 0, 0, 1], [0, 1, 1, 0]))
