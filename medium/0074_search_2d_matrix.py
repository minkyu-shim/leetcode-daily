# Problem: 74 search a 2d matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/description/
# Level: Medium
# Date: May 31th 2025
# Approach: Binary search

def search_matrix(matrix, target):
    first_nb_of_each_sub_matrix = [sub_list[0] for sub_list in matrix]
    target_sub_list_index = 0

    for i, x in enumerate(first_nb_of_each_sub_matrix):
        if x > target:
            target_sub_list_index = i - 1
            break
        target_sub_list_index = len(matrix) - 1
    return target in matrix[target_sub_list_index]


def binary_search_matrix(matrix, target):
    low, high = 0, len(matrix) - 1
    candidate_row = -1

    while low <= high:
        mid = (low + high) // 2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            candidate_row = mid
            break
        elif target < matrix[mid][0]:
            high = mid - 1
        else:
            low = mid + 1

    if candidate_row == -1:
        return False

    l, r = 0, len(matrix[candidate_row]) - 1
    while l <= r:
        m = (l + r) // 2
        if matrix[candidate_row][m] == target:
            return True
        elif target < matrix[candidate_row][m]:
            r = m - 1
        else:
            l = m + 1

    return False


ex1 = search_matrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
ex2 = search_matrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13)
ex3 = search_matrix([[1], [3]], 3)
print(ex1, ex2, ex3)
