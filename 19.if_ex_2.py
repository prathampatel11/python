 
farm_A_length= float(input("enter_the_farm_A_length ="))

farm_A_width= float(input("enter_the_farm_A_width ="))

farm_B_length= float(input("enter_the_farm_B_length ="))

farm_B_width= float(input("enter_the_farm_B_width ="))

farm_A_area = farm_A_length * farm_A_width


farm_B_area = farm_B_length * farm_B_width

if farm_A_area>farm_B_area:
    print("farm_A_is_bigger_than_farm_B")
    print("farm_A =",farm_A_area)

if farm_A_area<farm_B_area:
    print("farm_B_is_bigger_than_farm_A")
    print("farm_B =",farm_B_area)

if farm_A_area==farm_B_area: 
    print("farm_A_and_farm_B_is_same")
    print("farm_A =",farm_A_area)
    print("farm_B =",farm_B_area)

