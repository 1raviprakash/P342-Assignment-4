# Python modules made and imported here

import P_P
import F_B_SUB
import LU_DECO

# Solving question 1

# Opening matrices
with open('Q.1.1.TXT', 'r') as f:
    a = [[int(num) for num in line.split()] for line in f]

with open('Q.1.2.TXT', 'r') as f:
    b = [[int(num) for num in line.split()] for line in f]


# Pivoting the Augmented Matrix
e = P_P.func(a, b)

# LU decomposition of the matrix
LU_DECO.func(a)

# Forward Backward Substitution
x = F_B_SUB.func(a, b)

# Printing the Solution
print("Solution of the question 1:")
# matrixlib.write(x)
for r in x:
    print(r)


# Output
# Solution of the question 1:
# [1.0]
# [-1.0]
# [1.0]
# [2.0]
