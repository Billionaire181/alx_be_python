monthly_income = float(input("Enter your monthly income:"))
total_monthly_expenses = float(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - total_monthly_expenses
simple_annual_interest = 0.05
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are: {monthly_savings:.2f}")
print(f"Your projected savings after one year; with interest, is: {Projected_savings:.2f}")
