# def countone(arr):
#     n=len(arr)
#     low,high=0,n-1
#     while low<=high:
#         mid=low+(high-low)//2
#         if arr[mid]==1:
#             low=mid+1
       
#         else:
#             high=mid-1
#     return low
# arr=[1,0,0,0,1,1,1,1]
# print(countone(arr)) 
def count_ones(arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2   
        if arr[mid] == 1:
            # Move right to find the last 1
            low = mid + 1
        else:
            # Move left to find the first 0
            high = mid - 1

    return low  # 'low' is now the count of 1s 
arr = [1, 1, 1, 1, 0, 0, 0]
print(count_ones(arr))       