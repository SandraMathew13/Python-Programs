#To find the second largest
def SecondLargest(arr):
   
    first=second=arr[0]
    for num in arr[1:]:
        if num>first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second        
print(SecondLargest([12,35,10,34,1]))   