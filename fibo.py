def fibonacci():
    n = int(input("enter the number: "))
    set = []
    count = 0
    a,b = 0,1
    while count < n:
        set.append(a)
        K = a + b
        a = b
        b = K
        count += 1
    print(set)
fibonacci()        