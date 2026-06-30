def merge(arr, left, mid, right): 
    L = arr[left: mid + 1 ]
    R = arr[mid+1 : right + 1 ]

    i = j = 0

    k = left

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else: 
            arr[k] + R[j]
            j += 1

        k += 1
    
    while i < len(L): 
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        arr[k] = R[j]
        j += 1 
        k += 1

def mergeSort (arr, left, right): 
    if left < right : 
        mid = (left + right ) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

arr = [38, 27, 43, 3, 9, 82, 10]
mergeSort(arr, 0, len(arr) - 1)
print(arr)
