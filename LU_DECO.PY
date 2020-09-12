# Function for finding  LU Decomposition of matrix
def func(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            s = 0
            if(i <= j):
                for k in range(i):
                    s = s + (a[i][k] * a[k][j])
                a[i][j] = a[i][j] - s
            else:
                for k in range(j):
                    s = s + (a[i][k] * a[k][j])
                a[i][j] = (a[i][j] - s) / a[j][j]
