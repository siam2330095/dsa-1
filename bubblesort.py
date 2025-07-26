def bubble(arr):
    n=len(arr)  
               
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print("string is sorted order are:")
    for i ,string in enumerate(arr,0):
        print(f"string is {i} :{string}")
        
arr=['geek','quize','siam']
bubble(arr) 