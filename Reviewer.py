# Reviewer

age = int(input("Input age: "))
revenue = float(input("Input monthly revenue: "))
credit = int(input("Input credit score: "))
years = float(input("Input years in business: "))
has_defaults = bool(input("Has been filed for bankruptcy?: "))
col_name = input("Collateral name: ")
col_val = float(input("Collateral value: "))

max_loan = 0
base_fee = 0

#Baseline

if age >= 21 and years >= 2.0 and has_defaults == False:
    print("CONTINUE: Passed Baseline Requirements")
    if credit >= 720:
        max_loan = revenue * 3
        print("Maximum Loan: ",max_loan)
        if revenue >= 50000:
             base_fee = max_loan * 0.015
             print("Base Processing Fee: ", base_fee)
        else:
            base_fee = max_loan * 0.025
            print("Base Processing Fee: ", base_fee)

        # Collateral

        if col_val >= max_loan:
            print("CONTINUE: Sufficient Collateral value for ", col_name)
        else:
            print("REJECTED: Insufficient Collateral value for ", col_name)

        # Modulus Surcharge

        if col_val % 5000 != 0:
            base_fee = base_fee + 250
        else:
            print("No Surcharge")

    elif credit >= 620 and credit < 720:
        max_loan = 1.5 * revenue
        if years >= 5.0:
            base_fee = max_loan * 0.2
            print("Base Processing fee: ", base_fee)
        else:
            base_fee = max_loan * 0.035
            print("Base Processing fee: ", base_fee)
    elif credit < 620:
        print("REJECTED: Low Credit Score")
    else:
        print("INVALID")
else:
    print("REJECTED: High Risk Application or Ineligible Owner")
