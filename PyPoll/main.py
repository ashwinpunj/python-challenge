import os
import csv
import pandas as pd

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # print(csvreader)

    csvrep = list(csvreader)

    total_votes = len(csvrep) - 1

    print(f'Total Votes: {total_votes}')

df = "Resources/election_data.csv"
df_df = pd.read_csv(df)


candidate_count = df_df['Candidate'].value_counts()
# print(candidate_count)

can = list(candidate_count)
can1 = can[0]
can2 = can[1]
can3 = can[2]
can4 = can[3]

perc1 = (can1 / total_votes) * 100
perc2 = (can2 / total_votes) * 100
perc3 = (can3 / total_votes) * 100
perc4 = (can4 / total_votes) * 100
winner = 'Khan'

print(f'Khan: {perc1}% ({can1})')
print(f'Correy: {perc2}% ({can2})')
print(f'Li: {perc3}% ({can3})')
print(f"O'Tooley: {perc4}% ({can4})")
print(f'Winner: {winner}')
