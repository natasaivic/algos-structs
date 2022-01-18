# Bubble sort is sorting algorithm that works by repeatedly swapping 
# the adjacent elements if they are in wrong order.

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


arr = [7,8,18,12,14,10,5,29,22,20]
print(bubble_sort(arr))
