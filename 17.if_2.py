
purchase_price = float(input("Enter_product_purchase_price ="))
sales_price = float(input("Enter_product_sales_price ="))

difference = sales_price - purchase_price

if difference>0:
    print("profit amount is ",difference)


if difference<0:
    print("loss amount is ",difference)


if difference==0:
    print("no profit no loss")
