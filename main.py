sum=0
while(True):
    inputPrice=input("enter the price of your item: \n")
    if(inputPrice!='q'):
        sum=sum+int(inputPrice)
        print("The order so far is :{}".format(sum))

    else:
        print("your total order is {}".format(sum))
        print("\n THANK YOU VISIT AGAIN")
        break

