import numpy as np
# matrix 생성
# 결과
# [[1 1]
#  [1 3]]
test_m = np.matrix([[1, 1], [1, 3]])
print(test_m)
# matrix dimension
# 결과
# (2, 2)
print(test_m.shape)

A = np.matrix([[1, 0], [2, 5], [3, 1]])
B = np.matrix([[4, 0.5], [2, 5], [0, 1]])
# 1. Addition Matrix
# 결과
# [[ 5.   0.5]
# [ 4.  10. ]
# [ 3.   2. ]]
print(A+B)
# 2. Subtration Matrix
# 결과
# [[-3.  -0.5]
# [ 0.   0. ]
# [ 3.   0. ]]
print(A-B)
# 3. Schalar Multiplication
# 결과
# [[ 3  0]
# [ 6 15]
# [ 9  3]]
print(A*3)
# 4. Schalar Divition
# 결과
# [0.33333333 0.        ]
# [0.66666667 1.66666667]
# [1.         0.33333333]]
print(A/3)
# 5. Vector Multiplication
C = np.matrix([[2], [3]])
# 결과
# [[ 2]
# [19]
# [ 9]]
print(A*C)
# Vector와 곱하면 Vector가 된다.
# 6. Matrix Multiplication
# 결과
# [[ 1  2  3]
# [17 24 31]
# [ 6 10 14]]
D = np.matrix([[1, 2, 3], [3, 4, 5]])
print(A*D)
