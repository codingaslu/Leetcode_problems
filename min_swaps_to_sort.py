def min_swaps_to_sort(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    swaps = 0

    for i in range(n):
        if arr[i] != sorted_arr[i]:
            # Find the index of arr[i] in sorted_arr
            correct_index = sorted_arr.index(arr[i])
            # Swap arr[i] and arr[correct_index]
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
            swaps += 1

    return swaps

# Example usage:
arr = [4, 3, 2, 1]
result = min_swaps_to_sort(arr)
print("Minimum swaps required to sort the array:", result)
