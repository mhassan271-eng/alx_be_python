# استلام البيانات من المستخدم
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# حساب الادخار الشهري
monthly_savings = income - expenses

# حساب الادخار السنوي مع الفايدة (5%)
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# طباعة النتائج
print(f"Your monthly savings: {monthly_savings}")
print(f"Your projected savings after one year with 5% interest: 
{annual_savings}")

