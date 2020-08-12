import os
import csv

resources_path = os.path.join("Resources/" + "election_data.csv")

candidates = []
num_votes = 0
vote_counts = []

with open(resources_path) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_file)

    for row in csv_reader:

    
        num_votes = num_votes + 1

        candidate = row[2]


        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1

        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0

for count in range(len(candidates)):
    vote_percentage = int(vote_counts[count])/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {int(percentages[count])}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

write_file = f"pypoll_results_summary.txt"

#open write file
("analysis/PyPollAnalysis.txt", "w") as analysis:

#print analysis to file
analysis.write("Election Results\n")
analysis.write("--------------------------\n")
analysis.write(f"Total Votes: {num_votes}\n")
for count in range(len(candidates)):
    analysis.write(f"{candidates[count]}: {int(percentages[count])}% ({vote_counts[count]})\n")
analysis.write("---------------------------\n")
analysis.write(f"Winner: {winner}\n")
analysis.write("---------------------------\n")

#close file
analysis.close()