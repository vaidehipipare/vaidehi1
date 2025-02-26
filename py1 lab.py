distance = int(input("distance"))
amount = int(input("amount"))
mileage = int(input("mileage"))

totaldis = distance*2
mil = totaldis/mileage

ans = mil*amount

answer = ans/4
print(answer)

if (answer%5 ==0):   
    print("true")
    
else:   
     print("false")



       
