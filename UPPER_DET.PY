# Function for finding upper determinent.
def func(a):
    n = len(a)
    r = 1
    for i in range(n-2):
        r = r * a[i][i]
    r = r * (a[n-2][n-2] * a[n-1][n-1])
    return r
