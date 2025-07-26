def evenodd(arr):
    n=len(arr)
    even=[]
    odd=[]
    for i in range(n):
        if i%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])  
    even.sort()
    odd.sort(reverse=True)
    i=0
    for num in even:
        arr[i]=num
        i+=1
    for num in odd:
        arr[i]=num
        i+=1
arr=[1,2,3,4,5,6,5,4,4]
evenodd(arr)
print(' '.join(map(str,arr)))