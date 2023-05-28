def adaptive_partition_sort(arr, threshold=0):
    def quick_sort(arr, low, high):
        if low >= high:
            return

        # Use median-of-three method to choose pivot
        mid = (low + high) // 2
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]

        pivot = arr[mid]

        # Partition array
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1

            if i >= j:
                break

            arr[i], arr[j] = arr[j], arr[i]

        # Recursively sort subarrays
        if j - low + 1 <= threshold:
            merge_sort(arr, low, j)
        else:
            quick_sort(arr, low, j)

        if high - (j + 1) + 1 <= threshold:
            merge_sort(arr, j + 1, high)
        else:
            quick_sort(arr, j + 1, high)

    def merge_sort(arr, low, high):
        if low >= high:
            return

        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        # Merge subarrays
        left = arr[low: mid + 1]
        right = arr[mid + 1: high + 1]
        i = j = 0
        k = low
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    quick_sort(arr, 0, len(arr) - 1)
