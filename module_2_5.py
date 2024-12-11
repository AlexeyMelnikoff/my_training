
def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        list = []
        for j in range(m):
            list.append(value)
        matrix.append(list)
    return matrix

result1 = get_matrix(2, 2, 10)
print(result1)
result2 = get_matrix(3, 5, 42)
print(result2)
result3 = get_matrix(4, 2, 13)
print(result3)