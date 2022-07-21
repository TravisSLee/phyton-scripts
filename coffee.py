is_a_size = False
is_a_type = False
order = []
cost = 0.0
while is_a_size == False:
    size = input("What size of coffe you want? Small, Medium, or Large ")
    if size.lower() == "small":
        cost += 2.0
        is_a_size = True
        order.append(size.lower())
    elif size.lower() == "medium":
        cost += 3.0
        is_a_size = True
        order.append(size.lower())
    elif size.lower() == "large":
        cost += 4.0
        is_a_size = True
        order.append(size.lower())
    else:
        print("Not a size")
        continue

while is_a_type == False:
    type = input("What type of coffee you want? Brewed, Espresso, or Cold Brew ")
    if type.lower() == "brewed":
        cost += 2.0
        is_a_type = True
        order.append(type.lower())
    elif type.lower() == "espresso":
        cost += 0.5
        is_a_type = True
        order.append(type.lower())
    elif type.lower() == "cold brew":
        cost += 1.0
        is_a_type = True
        order.append(type.lower())
    else:
        print("Not a type")
        continue
        
flavor = input("What flavor you want? ")
if flavor.lower() != "none":
    cost += 0.5
    order.append(flavor.lower())
else:
    order.append(flavor.lower())

cost *= 1.15    
print(order)    
print("The total is " + str(cost))
