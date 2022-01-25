def add(arr, n, value):
    if len(arr) != n:
        return
    arr.append(value)
    n = n + 1

    i = n - 1
    parent = int((i-1)/2)
    while i > 0:     
        print(i)
        print(parent)
        
        if arr[parent] < arr[i]:
            temp = arr[parent]
            arr[parent] = arr[i]
            arr[i] = temp
        i = parent
        parent = int((i-1)/2)


def delete(arr, n):
    front = arr[0]
    arr[0] = arr[n]
    n = n - 1

    i = 0
    left = 2 * i + 1
    right = 2 * i + 2
    while left < n or right < n: 

        if left > n:
            break

        if right < n and arr[right] > arr[left]:
            temp = arr[i]
            arr[i] = arr[right]
            arr[right] = temp
            i = right
    
        elif left < n and arr[left] > arr[right]:
            temp = arr[i]
            arr[i] = arr[left]
            arr[left] = temp
            i = left

        else:
            break

    return front
