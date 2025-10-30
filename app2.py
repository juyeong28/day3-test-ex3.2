for i in range(100, 0, -1):
    num_str = str(i)
    result = ""
    
    for c in num_str:
        if c == '3':
            result += "짝"
    
        else:
            result += c
    
    print(result)
    