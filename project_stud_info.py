from getpass import getpass
while (True):
    #Login 
    print('Welcome')
    uname = input('Enter The Username :')
    pwd = int(getpass('Enter the Password :'))
 
    def login():
        if(uname == 'admin'):
            if(pwd ==1234):
                print('Login Success')
                home()
        else:
            print('invalid username and password')
    
    def home():
        h = int(input('1. Student Registration \n2. Studens Information :'))
        if (h==1):
            stud_r() 
        elif(h==2):
            stud_info()
        else:
            print('Enter valid key' ) 
    def stud_r():
        stud_id =input('Enter Student ID') 
        stud_name = input('Enter Student Name') 
        stud_age = input('Enter student age')
        f = open('stud_r.txt','a')
        f.write('\n'+stud_id+'\t' + stud_name + '\t' + stud_age +'\n')
        print("stored successfully")
    def stud_info():
        f = open('stud_r.txt')
        for i in f:
            print(i, end =' ')
    login()
    try:
        y = input('Do you want to continue Y/N :' )
        if (y == 'Y' ):
            continue;
        elif(y == 'N'):
            break;
        else:
            print('Enter valid key')
    except:
        print('Enter valid key')
            
            
    