#This is a prgram to input and calculate new 
#insurance policy information for customers in One Stop Insurance Company
#Chelsey Penton, Nov. 21, 2023

#Program Constants

NEXT_POL_NUM = 1994
BASIC_PREM = 869.00
ADD_CAR_DISC = 25/100
EXTRA_LIA_COV_RATE = 130.00
GLASS_COV_RATE = 86.00
LOAN_CAR_COV_RATE = 58.00
HST_RATE = 15/100
PRO_MONTHLY_FEE = 39.99

#Program Libraries

import datetime
CurDate = datetime.datetime.now



#Variables set to 0

InsurancePrem = 0
TotInsurancePremAfterTax = 0
Downpayment = 0
MonthlyPayment = 0

#Program Functions

def CalcInsurancePrem(NumCars):

    #Calculates Insurace Premium based on number of cars insured

    global AddCarCost
    AddCarRate = (NumCars - 1)*(BASIC_PREM*ADD_CAR_DISC)
    AddCarCost = BASIC_PREM*(NumCars-1) - AddCarRate
    InsurancePrem = BASIC_PREM + AddCarCost
   

    return InsurancePrem

def CalcHSTCosts(HST_RATE, TotInsurancePrem):

    #This calculates the cost of HST and applies it to total costs to calculate total insurance cost after taxes

    global HSTCost
    HSTCost = TotInsurancePrem * HST_RATE
    TotInsurWithTax = HSTCost + TotInsurancePrem
    return TotInsurWithTax 

def CalcMonthPay(Paymethod, PRO_MONTHLY_FEE, Downpayment, TotInsurancePremAfterTax):

    #Calculates Monthly payment based on payment method

    if PayMethod.upper() == "DOWNPAYMENT":
        MonthlyPay = ((TotInsurancePremAfterTax + PRO_MONTHLY_FEE) - Downpayment)/8
    elif PayMethod.upper() == "MONTHLY":
        MonthlyPay = (TotInsurancePremAfterTax + PRO_MONTHLY_FEE)/8
    else:
        MonthlyPay = 0

    return MonthlyPay



#User Inputs and validations (Choice validations as well)

while True:


    #Validation Lists and Claim Lists

    ApprovedProv = ["NL", "NS", "BC", "QC", "ON", "AB", "SK", "MB", "NB", "PE"]
    ApprovedPayMethods = ["Downpayment", "Full", "Monthly"]
    Allowed_Digits = set("1234567890")
    DateHistory = []
    CostHistory = []

    #User Inputs, exit at start.

    CustFirstName = input("Enter the cutomer first name (END to exit): ").title()

    #Loop Exit
    if CustFirstName.upper() == "END":
        break

    CustomerLastName = input("Enter the customer last name: ").title()
    Address = input("Enter the customer address: ").title()
    City = input("Enter the customer's city of residence: ").title()

    while True:
        Province = input("Enter the customer's province of residence (XX): ").upper()

        #Validation list at begining of inputs

        if Province == "":
            print("Error, Province cannot be blank, please re-enter")
        elif len(Province) != 2:
            print("Error, province must be abbreviated, please re-enter")
        elif Province not in ApprovedProv:
            print("Error, province is not in allowed list of provinces, please re-enter.")
        else:
            break

    PostalCode = input("Enter the customer's postal code: ")
    NumCars = int(input("Enter the number of cars being insured today: "))

    while True:

        PhoneNum = input("Enter customer phone number(9999999999): ")

        if PhoneNum == "":
         print("Phone number cannot be blank, please re-enter")
        elif len(PhoneNum) != 10:
            print("Phone number must be 10 digits, please re-enter")
        elif set(PhoneNum).issubset(Allowed_Digits) == False:
            print("Phone number contains invalid characters, please re-enter")
        else:
            break

    #Choices for Extra costs

    while True:
        ExtraLiaChoice = input("Will the customer want extra liability coverage? (Y/N): ").upper()

        if ExtraLiaChoice == "":
            print("Error, choice cannot be blank, please re-enter.")
        elif ExtraLiaChoice == "Y":
            ExtraLiaCost = EXTRA_LIA_COV_RATE
            break
        elif ExtraLiaChoice == "N": 
            ExtraLiaCost = 0
            break
        else:
            print("Invalid choice, please enter Y or N")

    while True:
        GlassChoice = input("Will the customer want glass coverage? (Y/N): ").upper()

        if GlassChoice == "":
            print("Error, choice cannot be blank, please re-enter.")
        elif GlassChoice == "Y":
            GlassCost = GLASS_COV_RATE
            break
        elif GlassChoice == "N": 
            GlassCost = 0
            break
        else:
            print("Invalid choice, please enter Y or N")

    while True:
        LoanChoice= input("Will the customer want Loaner car coverage? (Y/N): ").upper()

        if LoanChoice == "":
            print("Error, choice cannot be blank, please re-enter.")
        elif LoanChoice == "Y":
            LoanCost = LOAN_CAR_COV_RATE
            break
        elif LoanChoice == "N": 
            LoanCost = 0
            break
        else:
            print("Invalid choice, please enter Y or N")


    while True:
        PayMethod = input("Please enter if the customer will be paying today, would like monthly installments, or will be putting a down payment. (Full/Monthly/Downpayment): ").title()

        if PayMethod in ApprovedPayMethods:
            if PayMethod == "Downpayment":
                Downpayment = float(input("Enter the customer's down payment: "))
            break
        elif PayMethod == "":
            print("Error, payment choice cannot be blank, please re-enter.")
        else:
            Downpayment = 0
            break

        
        #Input Previous claim dates and costs

    while True:

        Claim_Cost = input("Enter the preivous claim costs(Type ENTER to exit): ").upper()
        
        if Claim_Cost == "ENTER":
            break
        
        Claim_Cost = float(Claim_Cost)

        Claim_Date = input("Enter the date of previous claims (YYYY-MM-DD)); ")
        Claim_Date = datetime.datetime.strptime(Claim_Date,"%Y-%m-%d")

        CostHistory.append(Claim_Cost)
        DateHistory.append(Claim_Date)
        
        
        
    #Calculations

    InsurancePrem = CalcInsurancePrem(NumCars)
    ExtraCosts = LoanCost + GlassCost + ExtraLiaCost
    TotInsurancePrem = ExtraCosts + InsurancePrem
    TotInsurancePremAfterTax = CalcHSTCosts(HST_RATE, TotInsurancePrem)
    MonthlyPayment = CalcMonthPay(PayMethod,PRO_MONTHLY_FEE, Downpayment, TotInsurancePremAfterTax)

    #Formating of Y/N choices on extra costs

    if ExtraLiaChoice == "Y":
        ExtraLiaDisplay = "Yes"
    else:
        ExtraLiaDisplay = "No"

    if GlassChoice == "Y":
        GlassDisplay = "Yes"
    else:
        GlassDisplay = "No"

    if LoanChoice == "Y":
        LoanDisplay = "Yes"
    else:
        LoanDisplay = "No"
    
    #Dsp for formatting

    PhoneNumDisplay = "(" + PhoneNum[0:3] + ")" + PhoneNum[3:6] + "-" + PhoneNum[6:]

    CustomerNameDsp = CustFirstName[0] + "." + CustomerLastName

    AddressLineOne = Address + "," + Province

    AddressLineTwo = City + "," + PostalCode

    InsurancePremDsp = "${:,.2f}".format(InsurancePrem)
    ExtraCostsDsp = "${:,.2f}".format(ExtraCosts)
    TotInsurancePremDsp = "${:,.2f}".format(TotInsurancePrem)
    HSTCostDsp = "${:,.2f}".format(HSTCost)
    TotInsurancePremAfterTaxDsp = "${:,.2f}".format(TotInsurancePremAfterTax)
    MonthlyPaymentDsp = "${:,.2f}".format(MonthlyPayment)
    DownpaymentDsp = "${:,.2f}".format(Downpayment)
    CurDateDsp = CurDate().strftime("%Y-%m-%d")


    #Formating to receipt 

    print()
    print(f"----------------------------------------------------------------------")
    print(f"One Stop Insurance Company                   Invoice date: {CurDateDsp:>11s}")
    print(f"Insurance Policy Receipt")                   
    print()
    print(f"{CustomerNameDsp:<16s}                      Number of Cars Insured Today: {NumCars:>2d}")             
    print(f"{PhoneNumDisplay:<16s}                         Extra Liability Coverage: {ExtraLiaDisplay:>3s}")
    print(f"{AddressLineOne:<16s}                                   Glass Coverage: {GlassDisplay:>3s}")
    print(f"{AddressLineTwo:<16s}                              Loaner Car Coverage: {LoanDisplay:>3s}")
    print()
    print(f"----------------------------------------------------------------------")
    print(f"Payment Method: {PayMethod:<11s}        Insurance Premium Cost: {InsurancePremDsp:>11s}")
    print(f"Down Payment Amount: {DownpaymentDsp:<11s}         Extra Coverage Costs: {ExtraCostsDsp:11s}")
    print(f"                                   -----------------------------------")
    print(f"                     Total Insurance Premium before Taxes: {TotInsurancePremDsp:>11s}")
    print(f"                                                      HST: {HSTCostDsp:>11s}")
    print(f"                                   -----------------------------------")
    print(f"                      Total Insurance Premium after Taxes: {TotInsurancePremAfterTaxDsp:>11s} ")
    print(f"                               Monthly Payment (8 months): {MonthlyPaymentDsp:>11s}")
    print(f"----------------------------------------------------------------------")
    print()
    print(f"Previous Claim History")
    print()
    print(f"                  Claim #     Claim Date    Amount")
    print(f"                 ------------------------------------")
    
    #Loop for previous claims
    if DateHistory:
        for i in range(len(DateHistory)):
            ClaimNum = i + 1
            ClaimDateDsp = datetime.datetime.strftime(DateHistory[i], "%Y-%m-%d")  
            ClaimCostDsp = "${:,.2f}".format(CostHistory[i])

            print(f"            {ClaimNum:<6d}      {ClaimDateDsp:<11s}      {ClaimCostDsp:>11s}")
        else:
            print()
            print(f"            Thank you for using One Stop Insurance Company!.")
        print()

print()
print("Thank you for using One Stop Insurance Company!")
        
        

        

        


    
    


    