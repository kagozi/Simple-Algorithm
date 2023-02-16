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


# unit tests can be run to check validity of the code:
assert max_in_row_min_in_col([[5, 16, 20], [9, 11, 18], [15, 16, 17]]) == [17]
assert max_in_row_min_in_col(
    [[100, 60, 20, 50], [70, 80, 10, 90], [10, 50, 44, 30]]) == [50]
assert max_in_row_min_in_col([[5]]) == [5]

