def findmissing(arr):
    max_value=max(arr)
    min_value=min(arr)
    missing=[]
    for num in range(min_value,max_value+1):
        found=False
        for a in arr:
            if a==num:
                found=True
                break
        if not found:
            missing.append(num)
    n=len(missing)
    for i in range(n):
        for j in range(0,n-i-1):
            if missing[j]>missing[j+1]:
                missing[j],missing[j+1]=missing[j+1],missing[j] 
    return missing