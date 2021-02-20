import numpy as np
# 1. 교환법칙 성립이 안됨. (Commutative)
A = np.matrix([[1, 2], [3, 4]])
B = np.matrix([[5, 6], [7, 8]])
print(A*B)
# 결과
# [[19 22]
# [43 50]]
print(B*A)
# 결과
# [[23 34]
# [31 46]]
# 2. 결합법칙은 성립이 됨. (Associative)
A = np.matrix([[1, 2], [3, 4]])
B = np.matrix([[5, 6], [7, 8]])
C = np.matrix([[8, 9], [2, 5]])
print((A*B)*C)
# 결과
# [[196 281]
# [444 637]]
print(A*(B*C))
# 결과
# [[196 281]
# [444 637]]
# 3. 힝등행렬 : 어떤 행렬에 항등행렬을 곱해도 값이 변하지 않음. (Identity Matrix)
I = np.identity(2)
# I = np.eye(2)
print(A)
# [[1 2]
# [3 4]]
print(A*I)
# 결과
# [[1. 2.]
# [3. 4.]]
print(I*A)
# 결과
# [[1. 2.]
# [3. 4.]]
# 4. 역행렬 : A라는 행렬과 곱해서 1을 만드는 행렬 (Inverse Matrix)
# 정방행렬일 경우에 역행렬이 존재함.
# A * A의 역행렬 = A의 역행렬 * A = I
D = np.matrix([[1, 2], [3, 4]]).astype(int)
D_inv = np.linalg.inv(A).astype(float)
print(D_inv)
# 결과
# [[-2.   1. ]
# [ 1.5 -0.5]]
print(D * D_inv)
# 항등행렬이 나올거라 예상했는데 왜 이런 결과가 나온것인지 이해가 안간다;;
# 손으로 풀때는 제대로 나오는데...
# [[1.00000000e+00 1.11022302e-16]
#  [0.00000000e+00 1.00000000e+00]]
# 위의 현상에 대한 numpy github issue
# 결론적으로 부동소수점 계산에 의해 위와 같은 결과가 나온다는 이야기
# https://github.com/numpy/numpy/issues/12397
# 5. 전치행렬
D = np.matrix([[1, 2], [3, 4]]).astype(int)
print(D.T)
# 결과
# [[1 3]
# [2 4]]
