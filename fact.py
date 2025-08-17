def factorial():
    n = int(input("Enter the number: "))
    if n == 1 or n == 0:
        print("1")
        return
    elif n < 0:
        print("number cannot be negative")
    for i in range(1,n+1):
        fact = 1
        fact *= i
    print(fact)
factorial()     