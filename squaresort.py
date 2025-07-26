def mysquare(number):
    left, right = 0, number
    
    while right - left >= 2:
        mid = (left + right) / 2
        print("left, mid, right", left, mid, right)
        #print("mid found ", mid)

        if mid*mid == number:
            return  mid
        elif mid*mid > number:
            right = mid
        else:
            left = mid 
mysquare(100) 
