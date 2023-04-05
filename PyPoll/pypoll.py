
import os
import csv
import pathlib
import collections
from collections import Counter

# Define variables
voters_candidates = []
votes_per_candidate = []

csvpath = pathlib.Path(r"C:\\Users\reeda\Class Work\week 3\Homework\PyPoll\Resources\election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read/skip header row first
    csvheader = next(csvfile)

    for row in csvreader:
        # Append candidates list
        voters_candidates.append(row[2])

    # Sort by ascending order then arrange
    sorted_list = sorted(voters_candidates)
    arrange_list = sorted_list

    #count votes per candidate and append to list
    count_candidate = Counter(arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # calculate the percentage of votes per candicate in 3 digital points
    for item in votes_per_candidate:

        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')

# Print to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")


# Export a text file 
file = os.path.join("output", r"C:\Users\reeda\Anna\learnpython\polldata.txt")
with open(file, "w") as csv_file:

    csv_file.write("Election Results\n")
    csv_file.write("-------------------------\n")
    csv_file.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    csv_file.write("-------------------------\n")
    csv_file.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    csv_file.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    csv_file.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    csv_file.write("-------------------------\n")
    csv_file.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    csv_file.write("-------------------------\n")    

