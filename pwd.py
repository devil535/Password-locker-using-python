
def pwd_checking():
    while True:
        usrch=input("\nPress   1. To Copy Your Password \n\t2. To See Your Password \n\t3. To See All Id \n\t4. To See All Id And Passwords \n==> ")
        if (int(usrch) == 1):
            account=input("\nEnter Your Id to Copy Password : \t")
            if account in password:
                pyperclip.copy(password[account])
                print("\nPassword of Your ",account, "copied to clipboard")
            else:
                print("\n",account , "Is not Found --- Try to save it")
            break
        elif (int(usrch) == 2):
            pwd_see()
            break
        elif (int(usrch)==3):
            n=0
            for key in password:
                n+=1
                print(str(n)+") "+ key)
            break
        elif (int(usrch)==4):
            m=0
            print("\nAll The Saved Id And Passwords Are \n\n ")
            for key,val in password.items():
                m+=1
                print(str(m)+") "+key +" ==> " + val)
            break    
            
        else:
            print("You Have Entered Wrong Input")
            continue
        
def pwd_see():
    account=input("\nEnter Your id to Copy Password : \t")
    seepass=password[account]
    print("Your Password Of " ,account ,"Is : " + seepass)
    

def pwd_manage():
    use=input("Enter Your Id to Save Ur Pass: \t")
    
    if use in password:
        while True:
            print("\nThis account ",use ,"already exists ")
            deci=input("\n\t Do u want u upadte your password (Y | N): ")
            if (deci=="y" or deci=="Y" or deci=="yes" or deci=="YES"):
                pas=input("Enter ur pass: \t")
                password[use]=pas
                print("Password of ",use," Successfully Updated... ")
                break
            elif (deci=="n" or deci=="N" or deci=="no" or deci=="NO"):
                print("Your password is not updated")
                break
            else:
                print("INVALID SELECTION")
    else:  
        pas=input("Enter ur pass: \t")
        password[use]=pas
        print("\n Your Password of " , use , "Successfully saved in pwd_manager---------")
    
    

import pyperclip,sys
password={"email":"joydev","fb":"kjgsf","twitter":"shfy"}
print("\n |----------------------*-------------------------|")
print("\n |-----+-----*    PASSWORD MANAGER    *----+------|")
print("\n |----------------------*-------------------------|")
print("\nSELECT OPTION \n 1.TO MANAGE YOUR PASSWORD\n 2.TO SEE YOUR PASSWORD \n 3.EXIT")
print("_____________________________________________________")


while True:
    inp=input("\n> Enter ur input: ")
    if (inp.isdecimal()):
        if (int(inp) == 1):
            pwd_manage()
            print("\n\n\t\t\t\t\t\t\t -----Thank You for using it \n")
        elif (int(inp) == 2):
            pwd_checking()
            print("\n\n\t\t\t\t\t\t\t -----Thank You for using it \n")
        elif (int(inp) == 3):
            break
        else:
            print(" Invalid input ")
    else:
        print(" Invalid Input ")

print("\n------Thank You ------ ") 
