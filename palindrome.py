def palindrome():
    s=str(input("Enter the number:"))
    n= len(s)//2
    i = 0
    j = len(s)-1
    for num in range (n):
        if s[i] != s[j]:
            print("not a palindrome")
            return
        i+= 1
        j-= 1
    print("is Palindrome")
palindrome()

            