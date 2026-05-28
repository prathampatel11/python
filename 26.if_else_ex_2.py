triangle_A_length= float(input("enter_the_triangle_A_length ="))

triangle_A_base= float(input("enter_the_triangle_A_base ="))

triangle_B_length= float(input("enter_the_triangle_B_length ="))

triangle_B_base= float(input("enter_the_triangle_B_base ="))

triangle_A_area = triangle_A_length * triangle_A_base


triangle_B_area = triangle_B_length * triangle_B_base

if triangle_A_area>triangle_B_area:
    print("triangle_A_is_bigger_than_triangle_B")
    print("triangle_A =",triangle_A_area)

else:
    print("triangle_B_is_bigger_than_triangle_A")
    print("farm_B =",triangle_B_area)

if triangle_A_area==triangle_B_area: 
    print("triangle_A_and_triangle_B_is_same")
    print("triangle_A =",triangle_A_area)
    print("triangle_B =",triangle_B_area)

