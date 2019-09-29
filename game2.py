print("!! Welcome to the Akshay's Game !!")
print("rule - Only 5 attempts\n       Only Integer Value")
while (True):
    i =5
    
    a = 20
    while (i >= 1):
        n = int(input("Plz Enter the number :\n"))
        if (n < 16 ):
            print("hided number is greter")
        #break;
        elif(n > 25):
            print("hided number is smaller ")
        #break;
        elif(a == n):
            print("You Won")
            print("number of attempts",-(i-6))
            break;   
        elif (n > 15 and n < 20):
            print(" close greter")
        elif( n > 20 and n < 25):
            print("close smaller")
        #break;
        else:
            print("wrong number")
        print("you have attempts",i-1)
        i -= 1
    print("Game over")
    break;
    