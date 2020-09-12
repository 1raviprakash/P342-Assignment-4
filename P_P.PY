# A function for doing partial pivoting of a matrix

def func(a, b):
    n = len(a)
    task = 0
    for r in range(0, n):
        if abs(a[r][r]) == 0:
            for r1 in range(r+1, n):
                if abs(a[r1][r]) > abs(a[r][r]):
                    task = task+1
                    for x in range(0, n):
                        d1 = a[r][x]
                        a[r][x] = a[r1][x]
                        a[r1][x] = d1
                    if(b != 0):
                        d1 = b[r]
                        b[r] = b[r1]
                        b[r1] = d1
    return task
