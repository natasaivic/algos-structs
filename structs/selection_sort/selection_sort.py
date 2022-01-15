# The selection sort algorithm sorts an array by repeatedly finding the minimum element 
# (considering ascending order) from unsorted part and putting it at the beginning. 

def selection_sort(niz):
    for i in range(len(niz)):
        for j in range(i+1, len(niz)):
            if niz[i] > niz[j]:
                temp = niz[i]
                niz[i] = niz[j]
                niz[j] = temp
    
    return f"The sortid list is: {niz}"

niz = [4, 1, 2, 5, 0, 99, -9]
print(selection_sort(niz))
