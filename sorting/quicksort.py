def quick_sort_improved(arr, start, end):
    if start >= end:
        return
    pivot = start
    left, right = start + 1, end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

    quick_sort_improved(arr, start, right - 1)
    quick_sort_improved(arr, right + 1, end)


def quick_sort(arr):
    quick_sort_improved(arr, 0, len(arr) - 1)


def quick_sort_improved_mid3(arr, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    if arr[start] > arr[mid]:
        arr[start], arr[mid] = arr[mid], arr[start]
    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    if arr[mid] > arr[end]:
        arr[mid], arr[end] = arr[end], arr[mid]

    left, right = start + 1, end
    arr[mid], arr[start] = arr[start], arr[mid]
    pivot = arr[start]

    while left <= right:
        while left <= end and arr[left] <= pivot:
            left += 1
        while right > start and arr[right] >= pivot:
            right -= 1
        if left > right:
            arr[right], arr[start] = pivot, arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

    quick_sort_improved_mid3(arr, start, right - 1)
    quick_sort_improved_mid3(arr, right + 1, end)

