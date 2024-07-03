menu = {'pizza' : 80,
        "pasta" : 70,
        "burger" : 60,
        "salad":  50 ,
        "coffee": 40}

print("welcome to the restaurent")

print("pizza  : rs80 \npasta : rs70\nburger : rs60\nsalad:  rs50\ncoffee: rs40")

order_total = 0
item_1 = input("first order name =")
if item_1 in  menu :
    order_total += menu[item_1]
    
    print(f"your item {item_1} has been added to your order" )
else :
    print(f"ordered item {item_1} is not avialable yet ")
    
another_order = input("do you want to add something more item?, yes/no ")
if another_order == "yes" :
    item_2 = input("name of the second item= ")
    if item_2 in menu :
        order_total  += menu[item_2]
        print(f"item {item_2} has been added to your order ")
    else :
        print(f"item {item_2} is not avialable ")
        
print(f"the total amount of thr order is {order_total}")
