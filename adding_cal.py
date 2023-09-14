# the adding calcultor for stores

sum = 0
while (True):
    UserInput = (input("Enter the item price or press q to Quite: \n"))
    if (UserInput != 'q'):
        sum = sum + int (UserInput)
        
        print (f"order total so far: {sum}")
        
    else:
        print(f"Your bill total {sum}. thank you for shopping with us")
        break    
    