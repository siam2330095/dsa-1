def checkoverlap(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    for i  in range(n-1):
       start1,end1=arr[i]
       start2,end2=arr[i+1]
       if start2<end1:
           return True
       elif start1<end2:
           return False
      
arr=[[1, 3], [5, 7], [2, 4], [6, 8]]
print(checkoverlap(arr))