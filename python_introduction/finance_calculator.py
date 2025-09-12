monthly_income = int(input("Enter your monthly income:"))
total_monthly_expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = total_monthly_expenses - monthly_income
simple_annual_interest = 0.05
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your projected savings after one year (with 5% interest): {Projected_savings:.2f}")
