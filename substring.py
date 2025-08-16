def string(s) :
    left = 0
    seen = set()
    max_len = 0

    for num in range(len(s)):
       
        while s[num] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[num])
        max_len = max(max_len, num - left + 1)

    print("maximum length:" + str(max_len) )
    
string("abcabcbb")