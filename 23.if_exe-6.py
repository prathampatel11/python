
ahmedabad_to_delhi_train_ticket =int(input("enter_the_train_ticket_price ="))
ahmedabad_to_delhi_distance =int(input("enter_the_distance ="))
petrol_price =int(input("enter_the_petrol_price ="))

ahmedabad_to_delhi_car_rate = ahmedabad_to_delhi_distance * petrol_price
print("ahmedabad_to_delhi_car_rate",ahmedabad_to_delhi_car_rate)

if ahmedabad_to_delhi_car_rate>ahmedabad_to_delhi_train_ticket:
    print("ahmedabad_to_delhi_toway_train_")
    print("this_is_cheaper_way_to_Go_delhi_by_train")

if ahmedabad_to_delhi_car_rate<ahmedabad_to_delhi_train_ticket:
    print("ahmedabad_to_delhi_toway_car_")
    print("this_is_cheaper_way_to_Go_delhi_by_car")