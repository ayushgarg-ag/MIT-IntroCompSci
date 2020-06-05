#Part C: Finding the right amount to save away
an_salary = float(input("Enter your starting annual salary: "))
total_cost = 1000000
portion_down_payment = .25
months = 36
bi_search_num = 0

low = 0.0
portion_saved = 0.5
high = 1.0
semi_annual_raise = .07
r = 0.04


def calculated_savings(por_saved):
  semi_annual_raise = .07
  current_savings = 0.0
  r = 0.04
  annual_salary = an_salary
  for month in range(1, 37):
    if (month % 6 == 0):
      annual_salary = annual_salary*(1 + semi_annual_raise)
    monthly_salary = annual_salary / 12.0
    current_savings = current_savings + (por_saved*monthly_salary)
    current_savings = current_savings*(1 + r/12.0)
  return current_savings


while (abs(portion_down_payment*total_cost - calculated_savings((portion_saved))) >= 100):
  if (portion_down_payment*total_cost > calculated_savings(portion_saved)):
    low = portion_saved
  else:
    high = portion_saved
  portion_saved = (low + high) / 2
  bi_search_num += 1
  if (bi_search_num > 13):
    print("It is not possible to pay the down payment in three years.")
    break

if (bi_search_num <= 13):
  print("Best Savings Rate: ", portion_saved)
  print("Steps in bisection search: ", bi_search_num)