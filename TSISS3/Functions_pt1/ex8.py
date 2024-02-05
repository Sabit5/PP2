def spy_game(nums):
    has_0 = False
    has_00 = False
    
    for num in nums:
        # searching for 0 0
        if num == 0:
           
            if not has_0:
                has_0 = True
            
            elif has_0 and not has_00:
                has_00 = True
        #searching for 7 after 0 0
        elif num == 7:
            if has_0 and has_00:
                return True
            
    # didn't find 007
    return False

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0]))  