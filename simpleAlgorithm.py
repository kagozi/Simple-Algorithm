def max_in_row_min_in_col(matrix):
    result = []
    for i, row in enumerate(matrix):
        max_val = max(row)
        min_val = min(matrix[j][row.index(max_val)]
                      for j in range(len(matrix)))
        if max_val == min_val:
            result.append(max_val)
    return result


matrix_str = input("Enter the matrix in the format [[1,2,3],[4,5,6],...]: ")
matrix = eval(matrix_str)

result = max_in_row_min_in_col(matrix)
print(result)
