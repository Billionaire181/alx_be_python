monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses
Projected_Savings = monthly_savings * 12 
Projected_Savings += Projected_Savings * 0.05
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings:.0f}.")
