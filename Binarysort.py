def binarysearch():
    arr = list(map(int,input("Enter the elements: ").split()))
    arr.sort()
    print(arr)
    key = int(input("Enter the value to search: "))
    
    low, high = 0 , len(arr)-1
    while low <high:
        mid = (low + high)// 2
        if arr[mid] == key:
            print(f"value {key} id found at index {mid}.")
            return
        elif key < mid:
            high = mid - 1
        else:
            low = mid + 1
    print(f"{key} in not found.")       
binarysearch()   

















    