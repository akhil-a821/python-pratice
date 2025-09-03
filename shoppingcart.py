foods=[]
prices=[]
total=0
while True:
 food=input("enter the food you want to buy.((q) to quit):")
 if food.lower()=="q":
    break
 else:
   food=foods.append(food)
   price=int(input("enter the price of the food:$"))
   total=total+float(price) 
   price=prices.append(price)
print("----your shopping cart----")   
print(f"items are:{foods}",end=" ")
print()
print(f"total price of {len(foods)} item is:${total}")
print("----thanks for shopping with us----")
