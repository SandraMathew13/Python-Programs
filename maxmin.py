def maxmin():
    n = list(map(int,input("Enter the elements : ").split()))
    low = high = n[0]

    for num in n[1:]:
        
        if num > high:
            high = num
        if num < low:
            low = num
    print("miminum : " , low)
    print("maximum : ", high)
maxmin()    