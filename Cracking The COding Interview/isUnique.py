def isUnique(x):
    b = {}
    for i in range(len(x)):
        if x[i] in b:
            return False
        b[x[i]] = x

    return True
