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


