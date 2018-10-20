#5
def add_vectors(vector1,vector2):
    sum = []
    if len(vector1)==len(vector2):
        for _ in range(len(vector1)):
            sum.append(vector1[_]+vector2[_])
        return sum

"""
vector1 = (1,2,3)
vector2=(1,2,3)

print(add_vectors(vector1,vector2))

print(add_vectors([1, 1], [1, 1]))
print(add_vectors([1, 2], [1, 4]))
print(add_vectors([1, 2, 1], [1, 4, 3]))
"""
#6
def scalar_mult(scalar,vector):
    new = []
    for _ in range(len(vector)):
        new.append(vector[_]*scalar)
    return new
"""
print(scalar_mult(5, [1, 2]))
print(scalar_mult(3, [1, 0, -1]))
print(scalar_mult(7, [3, 0, 5, 11, 2]))
"""
#7
def dot_product(vector1,vector2):
    sum = 0
    if len(vector1) == len(vector2):
        for _ in range(len(vector1)):
            sum += (vector1[_]*vector2[_])
        return sum
"""
print(dot_product([1, 1], [1, 1]))
print(dot_product([1, 2], [1, 4]))
print(dot_product([1, 2, 1], [1, 4, 3]))
"""
#8
def cross_product(vector1,vector2):
    cross = [0,0,0]
    if len(vector1) == len(vector2) == 3:
        cross[0] = vector1[1]*vector2[2]-vector1[2]*vector2[1]
        cross[1] = vector1[2]*vector2[0]-vector1[0]*vector2[2]
        cross[2] = vector1[0]*vector2[1]-vector1[1]*vector2[0]
    return cross
"""
print(cross_product([1,1,1],[2,2,2]))
print(cross_product([1,3,1],[1,0,2]))
"""

def seq_tool(list,index):
    new_list = list[:index]+list[index+1:]
    return new_list
