monthly_income = eval(input("Enter your monthly income: "))
total_monthly_expenses = eval(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${monthly_savings:.0f}. ")
print(f"Projected savings after one year, with interest, is: ${Projected_savings:.0f}. ")
