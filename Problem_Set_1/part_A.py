#Part A: House Hunting
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the portion of salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = .25
current_savings = 0.0
r = 0.04
monthly_salary = annual_salary / 12
months = 0

while (current_savings < portion_down_payment*total_cost):
  current_savings = current_savings + current_savings*(r/12)
  current_savings = current_savings + portion_saved*monthly_salary
  months = months + 1

print("Number of months:", months)