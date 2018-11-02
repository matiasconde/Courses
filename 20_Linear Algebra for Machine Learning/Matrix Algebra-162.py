## 2. Matrix Vector Multiplication ##

matrix_a = np.asarray([[0.7,3,9],[1.7,2,9],[0.7,9,2]],dtype=np.float32)
vector_b = np.asarray([[1],[2],[1]],dtype = np.float32)

ab_product = np.dot(matrix_a,vector_b)
print(ab_product)

## 3. Matrix Multiplication ##

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

product_ab = np.dot(matrix_a,matrix_b)
product_ba = np.dot(matrix_b,matrix_a)

## 4. Matrix Transpose ##

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

transpose_b = np.transpose(matrix_b)
transpose_a = np.transpose(matrix_a)
print(transpose_a)

print(np.transpose(transpose_a))

trans_ba = np.dot(transpose_b,transpose_a)
trans_ab = np.dot(transpose_a,transpose_b)

product_ab = np.dot(matrix_a,matrix_b)
print(np.transpose(product_ab))


## 5. Identity Matrix ##

i_2 = np.asarray([[1,0],[0,1]],dtype = np.float32)
i_3 = np.asarray([[1,0,0],[0,1,0],[0,0,1]],dtype = np.float32)

matrix_33 = np.asarray([[2,1,2],[1,1,1],[4,5,1]],dtype = np.float32)
matrix_23 = np.asarray([[3,3,1],[2,1,1]],dtype = np.float32)

identity_33 = np.dot(i_3,matrix_33)
identity_23 = np.dot(i_2,matrix_23)

print(identity_23,matrix_23)
print(identity_33,matrix_33)

## 6. Matrix Inverse ##

matrix_a = np.asarray([
    [1.5, 3],
    [1, 4]
])

def matrix_inverse_two(matrix):
    a=matrix[0,0]
    b=matrix[0,1]
    c=matrix[1,0]
    d=matrix[1,1]
    det = a*d-c*b
    if det!=0:
        inv_mat = np.asarray([[d,-b],[-c,a]],dtype=np.float32)/det 
        return inv_mat
    else: raise ValueError("The matrix isn't invertible")

inverse_a = matrix_inverse_two(matrix_a)
result = np.dot(inverse_a,matrix_a)
i_2 = np.asarray([[result[0,0].round(1),result[0,1].round(1)],[result[1,0].round(1),result[1,1].round(1)]],dtype=np.float32)
print(i_2)

## 7. Solving The Matrix Equation ##

coef = np.asarray([[30,-1],[50,-1]],dtype=np.float32)
res = np.asarray([[-1000],[-100]],dtype=np.float32)
inv_coef = np.linalg.inv(coef)
solution_x = np.dot(inv_coef,res)

print(solution_x)

## 8. Determinant For Higher Dimensions ##

matrix_22 = np.asarray([
    [8, 4],
    [4, 2]
])

matrix_33 = np.asarray([
    [1, 1, 1],
    [1, 1, 6],
    [7, 8, 9]
])

det_22 = np.linalg.det(matrix_22)
det_33 = np.linalg.det(matrix_33)