import numpy as np


'''
Steps:
Initialize an NxN matrix with zeros
Directions for movement: right, down, left, up
Starting position (center of the matrix)
Initial number to place in the matrix
Step count and direction index
Each step length is repeated twice before increasing
Move in the current direction
Change direction (right -> down -> left -> up)
Increase step size every two directions 
'''
def generate_spiral_matrix(N):
    matrix = np.zeros((N, N), dtype=int)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = N // 2, N // 2
    num = 1
    matrix[x, y] = num
    steps = 1
    direction_index = 0
    while num < N * N:
        for _ in range(2):  
            for _ in range(steps):
                if num >= N * N:
                    break
                x += directions[direction_index][0]
                y += directions[direction_index][1]
                num += 1
                matrix[x, y] = num
            direction_index = (direction_index + 1) % 4
        steps += 1
    return matrix

'''
Steps:
Calculate the sum of the primary diagonal
Calculate the sum of the secondary diagonal
'''
def diagonal_sums(matrix):
    N = len(matrix)
    primary_diagonal_sum = sum(matrix[i][i] for i in range(N))    
    secondary_diagonal_sum = sum(matrix[i][N - 1 - i] for i in range(N))
    return primary_diagonal_sum, secondary_diagonal_sum

'''Example'''
N = 5
matrix = generate_spiral_matrix(N)
print(matrix)

primary_sum, secondary_sum = diagonal_sums(matrix)
print(f"Primary diagonal sum: {primary_sum}")
print(f"Secondary diagonal sum: {secondary_sum}")
