weight_1 = float(input("enter the first person weight ="))
weight_2 = float(input("enter the second person weight ="))
weight_3 = float(input("enter the third person weight ="))

if weight_1>weight_2:
    
    if weight_1>weight_3:
        print("first person is heaviest person.")
    
    else:
        print("third person is heaviest person.")
        
elif weight_1 == weight_2:
    if weight_1 == weight_3:
        print("all three person are equal.")

else:
    if weight_2>weight_3:
        print("second person is heaviest person.")
        
    else:
        print("third person is heaviest person.")
