x = str(input("Enter Your Name: "))
y = int(input("Enter Your Password: "))
Current_Bal = 1000.00
if (y == 1111) and (x == "Binaansim" or "BINAANSIM" or "binaansim"):
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Financial Service")
    print("-----------------------------------------------------")
    z= int(input("Select one Option: "))
    if z==1: 
        print("Your balance is Ghc", Current_Bal )
        print()
        print()
        print("-----------------------------------------------------")
        print("Thank you very Much for using MTN MOMO")
    elif z==2: 
        print("How much are you depositing: ")
        a = int(input(": "))
        Current_Bal = Current_Bal + a
        print("Your Current Balance is ", Current_Bal)
        print()
        print()
        print("-----------------------------------------------------")        
        print("Thank you very Much for using MTN MOMO")
    elif z == 3:
        print("How much do you like to withdraw: ")
        c = int(input(": "))
        Current_Bal = Current_Bal - c
        print("Your Remaining balance is ", d)
        print()
        print()
        print("-----------------------------------------------------")        
        print("Thank you very Much for using MTN MOMO")
    elif z == 4: 
        print("Sorry, There is no service available at the moment")
        print("Please Try Again")
        print()
        print()
        print("-----------------------------------------------------")        
        print("Thank you very Much for using MTN MOMO")
    else: 
        print("What else will you like to do?")
        
else:
    print("Incorrect Password or Username")
    print("Please Try Again")
    
    
                
    