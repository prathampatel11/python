#  write a program to findout which is cheaper approach to buy IPhone 17 pro max. 
#  consider use is going usa should he buy iphone from usa or from india. 

iphone_USA_price =int(input("enter_the_iphone_USA_price ="))
iphone_USA_price = iphone_USA_price * 94.13

iphone_india_price =int(input("enter_the_iphone_india_price ="))
 
if iphone_USA_price<iphone_india_price:
    print("cheaper_iphone_is_usa_price")
    print("you_are_buying_iphone_in_USA")

if iphone_USA_price>iphone_india_price:
    print("cheaper_iphone_is_indian_price")
    print("you_are_buying_iphone_in_india")