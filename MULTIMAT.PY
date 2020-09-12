# Function for matrix multiplication (limited matrix)

# def mat_multi(a, b):
#     p2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#     n = len(a)
#     for x in range(n):
#         for i in range(n):
#             for y in range(n):
#                 p2[x][i] = p2[x][i] + (a[x][y] * b[y][i])
#     return p2


# Function for matrix multiplication of any matrix

def func(a, b):
    l = len(b)
    n = len(a)
    m = len(b[0])
    p2 = [[0 for y in range(m)] for x in range(n)]
    for x in range(n):
        for i in range(m):
            for y in range(l):
                p2[x][i] = p2[x][i] + (a[x][y] * b[y][i])
    return p2
