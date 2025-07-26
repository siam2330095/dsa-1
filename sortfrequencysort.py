from collections import Counter
def sort_frequency(arr):
    frequency=Counter(arr)

    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if (frequency[arr[j]]<frequency[arr[j+1]] ) or\
                frequency[arr[j]]==frequency[arr[j+1]] and arr[j]>arr[j+1] :
                    arr[j],arr[j+1]=arr[j+1],arr[j] 
    return arr
arr=[3,9,9,3,2,3]
print(sort_frequency(arr))