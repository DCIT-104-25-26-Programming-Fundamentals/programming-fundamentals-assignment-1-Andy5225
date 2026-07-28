# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# Function to read a matrix from the user
def read_matrix(rows, cols, name="Matrix"):
    matrix = []

    print(f"\nEnter values for {name}:")

    for i in range(rows):
        while True:
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))

            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Please enter exactly {cols} numbers.")

    return matrix


# Function to display a matrix neatly
def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:4}", end="")
        print()


# PART A: Function to transpose a matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []

        for i in range(rows):
            new_row.append(matrix[i][j])

        transpose.append(new_row)

    return transpose


# PART B: Function to add two matrices
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])

        result.append(row)

    return result


# PART C: Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    rows_a = len(matrix1)
    cols_a = len(matrix1[0])
    cols_b = len(matrix2[0])

    result = []

    for i in range(rows_a):
        row = []

        for j in range(cols_b):
            total = 0

            for k in range(cols_a):
                total += matrix1[i][k] * matrix2[k][j]

            row.append(total)

        result.append(row)

    return result


# Main program
def main():

    # ---------------- PART A ----------------
    print("PART A: Matrix Transpose")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    transposed = transpose_matrix(matrix)

    print("\nTransposed Matrix:")
    display_matrix(transposed)


    # ---------------- PART B ----------------
    print("\nPART B: Matrix Addition")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix1 = read_matrix(rows, cols, "Matrix A")
    matrix2 = read_matrix(rows, cols, "Matrix B")

    addition_result = add_matrices(matrix1, matrix2)

    print("\nMatrix A:")
    display_matrix(matrix1)

    print("\nMatrix B:")
    display_matrix(matrix2)

    print("\nAddition Result:")
    display_matrix(addition_result)


    # ---------------- PART C ----------------
    print("\nPART C: Matrix Multiplication")

    rows_a = int(input("Enter rows of Matrix A: "))
    cols_a = int(input("Enter columns of Matrix A: "))

    matrix_a = read_matrix(rows_a, cols_a, "Matrix A")


    rows_b = int(input("Enter rows of Matrix B: "))
    cols_b = int(input("Enter columns of Matrix B: "))

    # Check multiplication condition
    if cols_a != rows_b:
        print("Error: Columns of Matrix A must equal rows of Matrix B.")
        return

    matrix_b = read_matrix(rows_b, cols_b, "Matrix B")

    multiplication_result = multiply_matrices(matrix_a, matrix_b)

    print("\nMatrix A:")
    display_matrix(matrix_a)

    print("\nMatrix B:")
    display_matrix(matrix_b)

    print("\nMultiplication Result:")
    display_matrix(multiplication_result)


# Run program
if __name__ == "__main__":
    main()