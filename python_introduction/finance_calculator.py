ؤمثشق
# استلام البيانات من المستخدم
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# حساب الادخار الشهري
monthly_savings = monthly_income - monthly_expenses

# حساب الادخار السنوي مع الفايدة (5%)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# طباعة النتائج
print(f"Your monthly savings are: {monthly_savings}")
print(f"projected savings after one year, with interest, is: 
{projected_savings}")


