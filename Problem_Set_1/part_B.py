#Part B: Saving, with a raise
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(
    input("Enter the portion of salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

portion_down_payment = .25
current_savings = 0.0
r = 0.04
months = 0

while (current_savings < portion_down_payment*total_cost):
  monthly_salary = annual_salary / 12
  current_savings = current_savings + current_savings*(r/12)
  current_savings = current_savings + portion_saved*monthly_salary
  months = months + 1
  if (months % 6 == 0):
    annual_salary = annual_salary*(1 + semi_annual_raise)

print("Number of months:", months)