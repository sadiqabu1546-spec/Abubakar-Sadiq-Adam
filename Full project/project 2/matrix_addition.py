# Lab 4: Matrix Addition

# 1. Initialize Matrices (2D Lists)
matrix_A = [
    [1, 2],
    [3, 4]
]

matrix_B = [
    [5, 6],
    [7, 8]
]

# Initialize a 2x2 result matrix with zeros
result_matrix = [
    [0, 0],
    [0, 0]
]

# 2. Perform Addition using Nested Loops
for row_index in range(2): # Outer loop for rows
    for col_index in range(2): # Inner loop for columns
        # Sum corresponding elements
        result_matrix[row_index][col_index] = matrix_A[row_index][col_index] + matrix_B[row_index][col_index]

# 3. Print Matrix Function (Optional but good practice)
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ") # print space instead of newline
        print() # print a newline after each row

# 4. Display Results
print("Matrix A:")
print_matrix(matrix_A)

print("\nMatrix B:")
print_matrix(matrix_B)

print("\nSum of Matrices (A + B):")
print_matrix(result_matrix)
