def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left); merge_sort(right)

        index = index_left = index_right = 0

        while index_left < len(left) and index_right < len(right):
            if left[index_left] <= right[index_right]:
                arr[index] = left[index_left]; index_left += 1
            else:
                arr[index] = right[index_right]; index_right += 1
            index += 1

        while index_left < len(left):
            arr[index] = left[index_left]; index_left += 1; index += 1

        while index_right < len(right):
            arr[index] = right[index_right]; index_right += 1; index += 1


lis = [46, 13, 48, 47, 29, 44, 29, 3]
print(f"List -> {lis}")
merge_sort(lis)
print(f"Sorted list -> {lis}")