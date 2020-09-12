# Python modules made and imported here

import P_P
import F_B_SUB
import LU_DECO
import UPPER_DET
import MULTIMAT

# Solving question 2

# Opening matrices
with open('Q.2.1.TXT', 'r') as f:
    c = [[int(num) for num in line.split()] for line in f]

with open('IDENTITY.TXT', 'r') as f:
    identity = [[int(num) for num in line.split()] for line in f]

with open('Q.2.1.TXT', 'r') as f:
    d = [[int(num) for num in line.split()] for line in f]


# Pivoting the matrix
z = P_P.func(c, identity)

# LU decomposition
LU_DECO.func(c)

# Finding the determinant
p = UPPER_DET.func(c)
if(z % 2 == 0):
    print("The Determinant is :", p)
else:
    print("The Determinant is :", -1 * p)
# Inverse possible only if determinet is zero
if(p != 0):
    print("Inverse exists because here  determinant is non zero")
    # Doing Forward Backward Substitution
    x = F_B_SUB.func(c, identity)
    print("Solution of Question 2:")
    for r in x:
        print(r)
    # Inverse
    print("Taking the Inverse:")
    for r in (MULTIMAT.func(d, x)):
        print(r)

else:
    print("Inverse  do not exists for  determinant zero matrix")

# Output
# The Determinant is : -36.0
# Inverse exists if and only if  determinant is non zero
# Solution of Question 2:
# [-0.25000000000000006, 1.6666666666666672, -1.8333333333333333, 0.3333333333333333]
# [0.08333333333333337, -0.666666666666667, 0.8333333333333333, 0.0]
# [0.16666666666666666, -0.33333333333333326, -0.3333333333333333, 0.0]
# [-0.08333333333333333, 0.6666666666666666, 0.16666666666666666, 0.0]
# Taking the Inverse:
# [1.0, 0.0, 0.0, 0.0]
# [0.0, 1.0, 0.0, 0.0]
# [4.163336342344337e-17, -3.3306690738754696e-16, 0.9999999999999999, 0.0]
# [2.7755575615628914e-17, -2.220446049250313e-16, -2.7755575615628914e-16, 1.0]
