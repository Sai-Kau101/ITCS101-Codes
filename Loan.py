loan_amt = float(input("Input amount: "))
years = int(input("Input year/s: "))
month = years * 12
principal = loan_amt / month
remaining_bal = loan_amt

print(f"|\tMonth\t\t|\tMonthly Pay\t|\tPrincipal\t|\tRemaining Bal\t|\tLoan Interest\t|")
for x in range(1, month+1):
    remaining_bal -= principal
    loan_interest = remaining_bal * 0.00256
    monthly_pay = loan_interest + principal
    print(f"|\t{x}\t\t|\t{round(monthly_pay)}\t\t|\t{round(principal)}\t\t|\t{round(remaining_bal)}\t\t|\t{round(loan_interest)}\t\t|")
print()

# String Formatting (pattern)
# print(x, round(monthly_pay), round(principal, 2), round(remaining_bal, 2), round(loan_interest, 2))