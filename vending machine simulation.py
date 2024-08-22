print(f"~~~~~~~~~~Welcome to sayan's vending machine~~~~~~~~~~")
print(f"the available items are ")
print(f" Item A-$2 \n Item B-$3 \n Item C-$4")
while True:
    choice=input(f"so,what will you buy?..: ")
    price=int(input(f"enter the amount($) you wish to give: $"))
    if choice.lower()=="item a":
        if price==2:
            print(f"Dispensing item A.your change is ${price-2}")
        elif price>2:
            print(f"Dispensing item A.your change is ${price-2}")
        else:
            price2=int(input(f"Enter additional amount($): "))
            if price+price2==2:
              print(f"Dispensing item A.your change is ${price+price2-2}")
            elif price+price2>2:
              print(f"Dispensing item A.your change is ${price+price2-2}")
            else:
               print(f"transiction cancelled.choose again")
    elif choice.lower()=="item b":
        if price==3:
            print(f"Dispensing item A.your change is ${price-3}")
        elif price>3:
            print(f"Dispensing item A.your change is ${price-3}")
        else:
            price2=int(input(f"Enter additional amount($): "))
            if price+price2==3:
              print(f"Dispensing item A.your change is ${price+price2-3}")
            elif price+price2>3:
              print(f"Dispensing item A.your change is ${price+price2-3}")
            else:
               print(f"transiction cancelled.choose again")
    elif choice.lower()=="item c":
        if price==4:
            print(f"Dispensing item A.your change is ${price-4}")
        elif price>4:
            print(f"Dispensing item A.your change is ${price-4}")
        else:
            price2=int(input(f"Enter additional amount($): "))
            if price+price2==4:
              print(f"Dispensing item A.your change is ${price+price2-4}")
            elif price+price2>4:
              print(f"Dispensing item A.your change is ${price+price2-4}")
            else:
               print(f"transiction cancelled.choose again")
    a=input(f"want to use again?? press 'u' or want to exit?? press 'e': ")
    if a=="e" or a=="E":
        print(f"~~~~~~~~~Thank you for using . see you again~~~~~~~~~")
        break
