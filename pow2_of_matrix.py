def pow2_of_matrix():
    matrix = input()
    matrix=matrix.replace("[", "")
    matrix=matrix.replace("]", "")
    matrix=[[int(y) for y in x.split(' ')] for x in matrix.split(',')]
    matrix_length=len(matrix)
    for i in range(matrix_length):
        if matrix_length != len(matrix[i]):
            print("couldn't multiply")
            return
    res = [[0 for x in range(matrix_length)] for y in range(matrix_length)]
    for i in range(matrix_length):
        for j in range(matrix_length):
            for k in range(matrix_length):
                res[i][j] += matrix[i][k] * matrix[k][j]
    value=''
    for i,x in enumerate(res):
        value += str(x).replace(',', ' ')
        if i!=len(res)-1:
            value+=','
    value = value.replace("]", "")
    value = value.replace("[", "")
    print('['+value+']')
if __name__ == '__main__':
    pow2_of_matrix()
