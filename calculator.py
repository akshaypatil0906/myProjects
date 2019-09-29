#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#print("This is console module")
while (True):
 num1,num2 = input('enter first & second number "," separated :\n ').split(",")
 num1,num2 = int(num1),int(num2)
 # = int(input('enter 2nd number : '))
 opt = input('enter +-/* operator : ')
 if (opt  == '+'):
    if(num1== 2 and num2==3):
         print(' 11 number is correct, welcome Boss ')
    else:
         print('number is ',num1 + num2)
 elif ( opt == '-'):
      if(num1== 2 and num2 == 3):
          print(' 11 number is correct, welcome Boss')
      else:
          print('Number is ',num1-num2)
 elif (opt == '*'):
      if(num1== 2 and num2 == 3):
          print(' 11 number is correct, welcome Boss')
      else:
          print('Number is ',num1*num2)
 elif (opt == '/'):
       if(num1== 2 and num2 == 3):
          print(' 11 number is correct, welcome Boss')
       else:
          print('Number is ',num1//num2)  
 z = input(" Y to continue and N to stop:")
 if ( z == "Y" or "y"):
         continue;
 elif( z == "N" or "n"):
         break;

