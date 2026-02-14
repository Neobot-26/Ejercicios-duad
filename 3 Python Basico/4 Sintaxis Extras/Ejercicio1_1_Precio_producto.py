deduction=0
final_price=0
product_price=int(input("Enter the price of the product:"))
if product_price<100:
    deduction=product_price*0.02
else:
    deduction=product_price*0.1
final_price=product_price-deduction    
print(f"The final price is:{final_price}")