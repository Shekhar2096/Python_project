YourIncome =float(input("Enter your Income: "))

MarriedFlag= False

while not MarriedFlag:
    MarriedOrNot = input("Are you married: ")
    if MarriedOrNot == 'Y':
        Parterner_Income =float(input("Enter your parterner's Income: "))
        Total_Income= YourIncome+Parterner_Income
        print("\nTotal Salary: ", Total_Income)
        MarriedFlag=True
        break
    elif MarriedOrNot == 'N':
        Total_Income= YourIncome
        print("\nTotal Salary: ", Total_Income )
        MarriedFlag=True
        break
    else:
        print("Please enter Y or N")
        continue

def Income_Split(Total_Income):   
    Needs = (Total_Income * Needs_percent) /100
    print("\nYou should spend total of " + str(Needs) + " on your basic needs ")

    Wants = (Total_Income * Wants_percent) /100
    print("You should spend total of " + str(Wants) + " on your wants ")

    Saving = (Total_Income * Saving_percent) /100
    print("You must save " + str(Saving) + " of your income for better future ")
    
    return Needs , Wants, Saving

def Saving_BreakUp(Saving_percent):
    
    SavingFlag=False
    while not SavingFlag:
        ManualOrDefault = input("Want to go for defalt saving calulation(Y/N): ")         
        if ManualOrDefault == 'Y': 
            Share_Market =  (Saving * 30) / 100
            SIP =  (Saving * 40) / 100
            NPS =  (Saving * 15) / 100
            HealthandTerm_Insurance =  (Saving * 7.5) / 100
            LIC =  (Saving * 7.5) / 100
            print("##############################################")
            print("Saving Breakup: " +  "\nShare_Market: "+ str(Share_Market) + "\nSIP: " + str(SIP) + "\nNPS: " + str(NPS) + "\nHealthandTerm_Insurance: " + str(HealthandTerm_Insurance) + "\nLIC: " + str(LIC))
            print("##############################################")
            SavingFlag=True
            break
        elif ManualOrDefault == 'N': 
            Total_Percent_Flag = False
            while not  Total_Percent_Flag:
                Share_Market_percent= float(input("How much you want to save of your Income in \nShare_Market %:"))
                SIP_percent = float(input("SIP %:"))
                NPS_percent = float(input("NPS %:"))
                HealthandTerm_Insurance_percent = float(input("HealthandTerm_Insurance %:"))
                LIC_percent = float(input("LIC %:"))
                Total_Percent = float(Share_Market_percent+SIP_percent+NPS_percent+HealthandTerm_Insurance_percent+LIC_percent) 
                if Total_Percent == 100:
                    Share_Market =   (Saving * Share_Market_percent) / 100
                    SIP =  (Saving * SIP_percent) / 100
                    NPS =  (Saving * NPS_percent) / 100
                    HealthandTerm_Insurance =  (Saving * HealthandTerm_Insurance_percent) / 100
                    LIC =  (Saving * LIC_percent) / 100
                    print("#################################")
                    print("\nSaving Breakup: " +  "\nShare_Market: "+ str(Share_Market) + "\nSIP: " + str(SIP) + "\nNPS: " + str(NPS) + "\nHealthandTerm_Insurance: " + str(HealthandTerm_Insurance) + "\nLIC: " + str(LIC))
                    print("#################################")    
                    Total_Percent_Flag = True
                    break
                else:
                    print("Warning:: Sum of all percent can't be more than 100 %")
            SavingFlag=True
            break
        else:
            print("Please enter Y or N")
            continue            
                
def Wants_Split(Wants_percent):  
     
    Travelling = (Wants * 30) /100
    print("\nYou should spend total of " + str(Travelling) + " on Travelling ")

    Party = (Wants * 30) /100
    print("You should spend total of " + str(Party) + " on Party ")

    Shopping = (Wants * 40) /100
    print("You should spend total of " + str(Shopping) + " on Shopping ")
    print("#################################") 
    return Travelling , Party , Shopping
    
def HouseHold_Expenditure(Total_Income):
    
    HouseHold_Veg=(Needs * 2) /100
    print("\nVegetables: ", round(HouseHold_Veg,2))

    HouseHold_Fruits=(Needs * 2) /100
    print("Fruits: ", round(HouseHold_Fruits,2))

    HouseHold_Grocery=(Needs * 8.5) /100
    print("Grocery: ", round(HouseHold_Grocery,2))

    HouseHold_Gas=(Needs * 1) /100
    print("Gas: ", round(HouseHold_Gas,2))

    HouseHold_Electricity=(Needs * 2) /100
    print("Electricity: ", round(HouseHold_Electricity,2))

    HouseHold_Utility_Bills=(Needs * 3) /100
    print("Phone and Internet Bills: ", round(HouseHold_Utility_Bills,2))

    HouseHold_Fuel=(Needs * 7) /100
    print("Fuel: ", round(HouseHold_Fuel,2))

    HouseHold_Extra=(Needs * 8) /100
    print("Extra: ", round(HouseHold_Extra,2))

    HouseHold_Maid=(Needs * 2) /100
    print("Maid: ", round(HouseHold_Maid,2))

    TotalOnHouseHold=HouseHold_Veg+HouseHold_Fruits+HouseHold_Grocery+HouseHold_Gas+HouseHold_Electricity+HouseHold_Utility_Bills+HouseHold_Fuel+HouseHold_Extra+HouseHold_Maid
    print("\nTotal expenditure on HouseHold :", round(TotalOnHouseHold,2))
      
    CCFlag = False
    while not CCFlag: 
        CCBillOrNOT = input("Is there any Credit Card Bill(Y/N): ")
        if CCBillOrNOT =='Y':
            CCBill = float(input("Enter Credit Card Amount: "))
            CCFlag=True
            break
        elif CCBillOrNOT =='N':
            CCBill =0
            CCFlag=True
            break
        else:
            print("Please enter Y or N")
            continue
        
    LoanFlag = False
    while not LoanFlag:
        HomeLoanOrNot = input("Do You have any Home Loan(Y/N): ")        
        if HomeLoanOrNot == 'Y':
            HomeLoanAmt = float(input("Enter Home Loan Amount: "))
            RemaningAmtFromNeeds = Needs - (TotalOnHouseHold+CCBill+HomeLoanAmt)
            LoanFlag=True
            break
        elif HomeLoanOrNot == 'N':
            HouseRent = float(input("Enter House Rent Amount: "))
            RemaningAmtFromNeeds = Needs - (TotalOnHouseHold+CCBill+HouseRent)
            LoanFlag=True
            break
        else:
            print("Please enter Y or N")
            continue
        
    print("\nRemaining Amt from Needs :", RemaningAmtFromNeeds)
    
    if RemaningAmtFromNeeds > 0:
        print("Yayyyy, you can buy something for your loved one ")
    else:
        print("You should spent on your needs carefully onwards ")
    


Total_Percent_Flag = False

while not  Total_Percent_Flag:
    ManualOrDefault= input("Want to go for defalt calulation(Y/N): ")
    if ManualOrDefault =='Y':
        Saving_percent=35
        Needs_percent= 55
        Wants_percent= 10
        Total_Percent= int(Saving_percent+Needs_percent+Wants_percent)
        Needs,Wants,Saving=Income_Split(Total_Income)      
        HouseHold_Expenditure(Total_Income)
        Saving_BreakUp(Saving_percent)
        Wants_Split(Wants_percent)
        Total_Percent_Flag = True
        break
    elif ManualOrDefault =='N':
        Saving_percent= float(input("How much you want to save of your Income in %: "))
        Needs_percent = float(input("How much you want to spend on your needs in %: "))
        Wants_percent = float(input("How much you want to spend on your wants in %: "))
        Total_Percent1 = float(Saving_percent+Needs_percent+Wants_percent)
        if Total_Percent1 == 100:
            Needs,Wants,Saving=Income_Split(Total_Income)
            HouseHold_Expenditure(Total_Income)
            Saving_BreakUp(Saving_percent)
            Wants_Split(Wants_percent)
            Total_Percent_Flag = True
            break
        else:
            print("Warning:: Sum of all percent can't be more than 100 %")
    else:
        print("Please enter Y or N")
        continue

print("its done")

