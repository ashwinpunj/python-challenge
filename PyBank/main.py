import csv
import os
import pandas as pd

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    csvrep = list(csvreader)

    num_months = len(csvrep) - 1
    print(f'Total Months: {num_months}')

df = "Resources/budget_data.csv"
df_df = pd.read_csv(df)
# print(df_df)

net_total = df_df['Profit/Losses'].sum()
print(f'Total: {net_total}')

avg_change = ((df_df.iloc[num_months - 1, 1]) -
              (df_df.iloc[0, 1])) / (num_months - 1)


print(f'Average Change: {avg_change}')


n = 0
m_diff = []
while n <= (num_months - 2):
    diff = df_df.iloc[n + 1, 1] - df_df.iloc[n, 1]
    m_diff.append(diff)
    n = n + 1

# print(m_diff)
max_diff = max(m_diff)
min_diff = min(m_diff)
max_date = df_df.iloc[m_diff.index(max_diff) + 1, 0]
min_date = df_df.iloc[m_diff.index(min_diff) + 1, 0]


print(f'Greatest Increase in Profits: {max_date} (${max_diff})')
print(f'Greatest Decrease in Profits: {min_date} (${min_diff})')
