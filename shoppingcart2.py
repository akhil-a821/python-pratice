menue={"tomato":10,"potato":20,"onion":30,"carrot":40}
cart=[]
total=0
print("------menue------")
for key,value in menue.items():
    print(f"{key}:{value}")
print("-----------------")    
while True:
   food=input("enter the food you want to purchase(done to stop):")
   if food=="done":
       break
   elif food in menue is not None:
       cart.append(food)
print("your cart items are:",cart)
for food in cart:
 total=total+menue.get(food)
print(f"your total bill is:{total:.2f}")
       