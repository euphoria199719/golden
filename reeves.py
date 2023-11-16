import numpy as np

def get_matrix(rows, cols):
    matrix = []
    print(f"Enter {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)

def print_menu():
    print("Matrix Operations Menu:")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Scalar Matrix Multiplication")
    print("4. Elementwise Matrix Multiplication")
    print("5. Matrix Multiplication")
    print("6. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '6':
            break

        rows1 = int(input("Enter the number of rows for Matrix 1: "))
        cols1 = int(input("Enter the number of columns for Matrix 1: "))
        matrix1 = get_matrix(rows1, cols1)

        if choice in ['1', '2', '4', '5']:
            rows2 = int(input("Enter the number of rows for Matrix 2: "))
            cols2 = int(input("Enter the number of columns for Matrix 2: "))
            matrix2 = get_matrix(rows2, cols2)

        if choice == '1':
            result = np.add(matrix1, matrix2)
        elif choice == '2':
            result = np.subtract(matrix1, matrix2)
        elif choice == '3':
            scalar = float(input("Enter the scalar value: "))
            result = np.multiply(matrix1, scalar)
        elif choice == '4':
            result = np.multiply(matrix1, matrix2)
        elif choice == '5':
            if cols1 != rows2:
                print("Matrix multiplication is not possible. Number of columns in Matrix 1 must be equal to the number of rows in Matrix 2.")
                continue
            result = np.matmul(matrix1, matrix2)
        
        print("Result:")
        print(result)

if __name__ == "__main__":
    main()
