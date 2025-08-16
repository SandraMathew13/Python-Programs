def string(s) :
    left = 0
    seen = set()
    max_len = 0

    for num in range(len(s)):
       
        while s[num] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[num])
        #max_len = max(max_len, num - left + 1)
        curr_length = num - left +1
        if curr_length > max_len:
            max_len = curr_length
            result = [s[left : num +1]]
        if curr_length == max_len:
            result.append(s[left : num +1])
    print("Strings :" , result) 
    
    
string("abcabcbb")