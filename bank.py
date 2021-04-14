accountNum = 0
accounts=[]
money = []
def conditions(c): #switch case for deciding what to do
    if c==0:
        print("Program written by Jai Shah, thanks for using !")
        exit()
    elif c==1:
        openAcc()
    elif c==2:
        deposit()
    elif c==3:
        withdraw()
    elif c==4:
        display()
    else:
        print("Wrong input !\n")

def openAcc(): #open new user account
    global accounts, accountNum
    print("Enter name of account holder: ",end="")
    name = input()
    accounts.append(name)
    accountNum += 1
    money.append(0.0)
    print("Account number: "+str(accountNum)+" created succesfully !\n") 

def deposit(): #deposit money into existing account
    global accounts, money
    print("Enter name or account number: ",end="")
    accNum = input()
    try:
        accNum = int(accNum)
    except:
        accNum = str(accNum)
    if type(accNum)==int:
        temp = int(int(accNum)-1) #reducing 1 because of indexing
    else:
        try: 
            temp = int(accounts.index(accNum))
        except:
            print("Error 1 occured")
            exit(0)
    print("Enter amount to be deposited: ",end="")
    amount = float(input())
    try:
        money[temp] = money[temp]+amount
    except:
        print("Error 2 occured")
        exit(0)
    print("Amount deposited !\n")

def withdraw(): #withdraw money from existing account
    global accounts, money
    print("Enter name or account number: ",end="")
    accNum = input()
    try:
        accNum = int(accNum)
    except:
        accNum = str(accNum)
    if type(accNum)==int:
        temp = int(int(accNum)-1) #reducing 1 because of indexing
    else:
        try: 
            temp = int(accounts.index(accNum))
        except:
            print("Error 3 occured")
            exit(0)
    print("Enter amount to be withdrawn: ",end="")
    amount = float(input())
    if money[temp]>amount:
        try:
            money[temp] = money[temp]-amount
            print("Amount withdrawn !\n")
        except:
            print("Error 4 occured")
            exit(0)
    else:
        print("Insufficient balance !\n")
    
def display(): #display account holder name and balance
    global accounts, money
    print("Enter name or account number: ",end="")
    accNum = input()
    try:
        accNum = int(accNum)
    except:
        accNum = str(accNum)
    if type(accNum)==int:
        temp = int(int(accNum)-1) #reducing 1 because of indexing
    else:
        try: 
            temp = int(accounts.index(accNum))
        except:
            print("Error 3 occured")
            exit(0)
    print("Account holder name: "+accounts[temp])
    print("Account Balance: "+str(money[temp])+"\n")


# Driver code
print("********** Welcome to JS Bank ! **********")
choice = 5
while(choice!=0):
    print("Please select an option: ")
    print("\n\t 1. Open account \n\t 2. Deposit money \n\t 3. Withdraw money \n\t 4. Display account \n\t 0. Exit")
    print("***************************************")
    print("Enter your choice: ",end="")
    choice = int(input())
    conditions(choice)