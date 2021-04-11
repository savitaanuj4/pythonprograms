#Program for selection sort

def sort(arr):
    
    for i in range(len(arr)-1):
        
        minpos = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[minpos]:
                minpos = j
        arr[i], arr[minpos] = arr[minpos], arr[i]
        
    return arr
    
a = [78,90,45,23,46,12,34,22,39]
print(sort(a))
