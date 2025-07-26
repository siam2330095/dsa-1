def selection_desending(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
             if arr[j]>arr[mini]:
                mini=j
                arr[i],arr[mini]=arr[mini],arr[i] 

def first_occu(arr,target):
    low,high=0,len(arr)-1
    first=-1 
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            first=mid 
            high=mid-1
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return first     
def last_occu(arr,target):
    low,high=0,len(arr)-1
    last=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            last=mid
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return last


def occure_count(arr,target):
    first=first_occu(arr,target)
    last= last_occu(arr,target)
    if first==-1:
        return 0
    return last-first+1
arr=['d','c','d','d']
selection_desending(arr)
print("started array",arr) 
target='d'
count=occure_count(arr,target)
print(count) 

