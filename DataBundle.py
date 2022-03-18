""" 
List all data plans
When the user selects a data plan, ask if they want to bundle or not.
If they want to bundle, display "You have bundled successfully"
If they don't want to bundle, display "Subscription cancelled"
"""
# These are the data bundles I'll look into
""" 
List of Data bundles:
     Daily data plan
     Weekly data plan
     Monthly data plan
"""


# User dials *131# >>> MTN Code for Data bundle
print("MTN DATA BUNDLE")
print()
  
dail_code = int(input("Dail Code:  "))
print()

def mainmenu():
    print("1. Data Plans")
    print("2. Balance Check")
    print("3. Cancel")


def balancecheck():
    print("Data balance is left with 816MB")
    exit = int(input("Press 0 to return to mainmenu: "))
    mainmenu()

def dataplan():
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    dataoption = int(input("Enter 1 - 3 to proceed with subcription: "))
    
    if dataoption == 1:
        dailyPlan()
    elif dataoption == 2:
        weeklyPlan()
    elif dataoption == 3:
        monthlyPlan () 
    else:
        print("Invalid option. Enter option between 1 - 3")
        mainmenu()  

def dailyPlan():
    print("1. N50 for 40 MB") 
    print("2. N100 for 100 MB")
    selectedplan = int(input("Enter 1 - 2 to select a plan: "))
    print(f"Do you want to bundle,{selectedplan} ?")
    print ("1. Yes")
    print ("2. No")
    option = int(input("Select an option "))
    if option == 1 :
        print(f"You have successfully bundled, {selectedplan}")
    elif option == 2:
        print("Subscription Cancelled")
    else:
        dataplan()
    

def weeklyPlan():
    print("1. N200 for 1GB")
    print("2. N500 for 1.5G")
    selectedplan = int(input("Enter 1 - 2 to select a plan: "))
    print(f"Do you want to bundle {selectedplan} ?")
    print ("1. Yes")
    print ("2. No")
    option = int(input("Select an option "))
    if option == 1:
        print(f"You have successfully bundled {selectedplan}")
    elif option == 2:
        print("Subscription Cancelled")
    else:
        dataplan()

def monthlyPlan():
    print("1. N1,000 for 1.5GB") 
    print("2. N1,200 for 2GB")
    selectedplan = int(input("Enter 1 - 2 to select a plan: "))
    print(f"Do you want to bundle {selectedplan} ?")
    print ("1. Yes")
    print ("2. No")
    option = int(input("Select an option "))
    if option == 1:
        print(f"You have successfully bundled {selectedplan}")
    elif option == 2:
        print("Subscription Cancelled")    
    else:
        dataplan()    

# I'll call out the mainmenu function 
mainmenu()

# Exception handling using try >> except clause used in the while loop.

while True:
    try:
        option = int(input("\n Select option: "))
        if option == 1:
            dataplan()
            break
        elif option == 2:
            balancecheck()
            break
        elif option == 3:
            break
        else:
            print("Invalid option. Enter option between 1 - 3")
            mainmenu()       
    except ValueError:
         print("Invalid option, Please enter option between 1 - 3: ")
exit






        



















