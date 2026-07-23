'''birth_year=int(input("Enter year of birth"))
age=2026-birth_year
print("Age=",age)'''

birth_year=int(input("Enter year of birth"))
birth_month=int(input("Enter month of birth"))
birth_day=int(input("Enter day of birth"))
age=2026-birth_year
current_month=7
current_day=24
if (current_month,current_day)<(birth_month,birth_day):
    age=age-1
print("Age=",age)