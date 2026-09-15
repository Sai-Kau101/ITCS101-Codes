# age (integer) 
# is_employed (boolean) 
# credit_score (integer) 
# annual_income (float) 
# has_collateral (boolean)

print("Loan")

age = int(input("Input your age: "))
is_employed = bool(input("Are you employed? True/False: "))
credit_score = int(input("Input your credit score: "))
annual_income = float(input("Enter your annual income: "))
has_collateral = bool(input("Do you have a collateral? True/False"))

base_rate = 0.0
print(" ")
print("Are you qualified?")

if age >= 21 and is_employed == True:
    print("\"Qualified to loan\", Continue")
    print(" ")
    if credit_score >= 750:
        print("You have a high credit score.")
        base_rate = 5.0
        if annual_income >= 100000:
            print("You have a high annual salary.")
            base_rate = 4.5
            print("Your base rate: ", base_rate)
        else:
            base_rate = 5.0
            print("Your base rate: ", base_rate)
    elif credit_score >= 600 and credit_score < 750:
        print("Your credit score is less than 750.")
        if has_collateral == True:
            print("You have a collateral.")
            base_rate = 7.0
            print("Your base rate: ", base_rate)
        elif annual_income <= 40000:
            print("Low annual income")
            base_rate = 9.0
            print("Your base rate: ", base_rate)
    elif credit_score < 600:
        print("Rejected, credit score too low.")
else:
    print("\"Rejected: Fails Baseline Criteria.\"")