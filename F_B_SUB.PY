# Function for finding F&B Substitution
def func(a, b):
    n = len(a)
    m = len(b[0])
    # Doing forward substitution first
    # For getting [[0,0,0,m times],for getting this n times]
    y = [[0 for y in range(m)] for x in range(n)]

    for i in range(n):
        for j in range(m):
            s = 0
            for k in range(i):
                s = s + a[i][k] * y[k][j]
            y[i][j] = b[i][j] - s
    # Doing backward  substitution then
    x = [[0 for y in range(m)] for x in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m):
            s = 0
            for k in range(i + 1, n):
                s = s + a[i][k] * x[k][j]
            x[i][j] = (y[i][j] - s) / a[i][i]

    return x
