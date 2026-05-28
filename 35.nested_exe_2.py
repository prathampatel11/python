height_1 = float(input("enter the first person height ="))
height_2 = float(input("enter the second person height ="))
height_3 = float(input("enter the third person height ="))
height_4 = float(input("enter the fourth person height ="))

if height_1>height_2:
    
    if height_1>height_3:
       
        if height_1>height_4:
            print("first person is tallest person.")
       
        else:
            print("fourth person is tallest person.")
   
    else:
         print("third person is tallest person.")

elif height_1 == height_2:
    if height_1 == height_3:
        if height_1 == height_4:
            print("All four person are equal")

elif height_2>height_3:

         if height_2>height_4:
            print("second person is tallest person.")

         else:
            print("fourth person is tallest person.")

else:
    if height_4>height_3:
      print("fourth person is tallest person.")
    
    

             
     
        
             
      