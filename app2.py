for i in range(100, 0, -1): 
    str_num = str(i)  
    count_3 = str_num.count('3')  
    
    if count_3 > 0:
        print("짝" * count_3)  
    else:
        print(i)  