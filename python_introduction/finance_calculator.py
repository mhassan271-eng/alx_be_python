
# استلام البيانات من المستخدم
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# حساب الادخار الشهري
monthly_savings = income - expenses

# حساب الادخار السنوي مع الفايدة (5%)
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# طباعة النتائج
print(f"Your monthly savings are: {monthly_savings}")
print(f"projected savings after one year, with interest, is: 
{Projected_Savings}")



