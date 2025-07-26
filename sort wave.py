def wave_sort(arr):
    n=len(arr)
    for i in range(n-1):
        if i%2==0:
            if arr[i]<arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        else:
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i] 
    return arr
arr=[10,5,6,3,2,20,100,80]
print(wave_sort(arr))