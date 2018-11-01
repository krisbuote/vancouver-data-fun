### 
# A simple script to visualize Vancouver's Government Employee Remuneration.
# The data contains all employee's salaries who exceed $75,000/year.
# I was curious if one department received higher wages than others.

###
# Author: Kristopher Buote


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/2017StaffRemunerationOver75KWithExpenses.csv", skiprows=2, header=1, thousands=',')
df['Remuneration'] = df['Remuneration'].apply(pd.to_numeric)
print(df.head())

groups = df.groupby(['Department'])['Remuneration'].agg('sum')
print(groups)

employee_counts = df.Department.value_counts()
print(employee_counts)

remuneration_total = groups.sum()
avg_salary = remuneration_total/employee_counts.sum()
print('The total income of Vancouver Government employees who make over 75K / year:', remuneration_total)
print('The average salary of Vancouver Government employees who make over 75K / year:', avg_salary)

income_distribution = dict()
average_salary_by_dept = dict()

for dept, value in groups.items():
	income_distribution[dept] = value/remuneration_total
	average_salary_by_dept[dept] = value/employee_counts[dept]

plt.figure(1)
plt.pie(list(income_distribution.values()), labels=list(income_distribution.keys()))
plt.axis('equal')
plt.title('Vancouver Department Income Distribution from Employees Making >75K/year', fontsize=14)
plt.text(x=-0.75, y=-1.4, fontsize=12, s="Total income from employees making >75K/year: ${0}".format(int(remuneration_total)))

plt.figure(2)
plt.pie(list(average_salary_by_dept.values()), labels=list(average_salary_by_dept.keys()))
plt.axis('equal')
plt.title("Average Salary Comparison of goverment workers making above 75K/year", fontsize=14)
plt.text(x=-0.75, y=-1.4, fontsize=12, s="Average Salary of Employees making >75K/year: ${0}".format(int(avg_salary)))


plt.show()

