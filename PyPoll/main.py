# Modules
import os
# Module for reading CSV files
import csv
# set path for file
csv_elec_path = os.path.join("Resources","election_data.csv")
# setting up the variables
# List for candidates
candidates = []
# List for the corresponding votes
votes = []
# Creating list for corresponding percentage votes
Percent_votes = []
# counter for total votes
total_vote = 0
# Reading the CSV file
with open(csv_elec_path, newline="") as csvfile:
# splitting the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
# Reading Header row of CSV file
    header = next(csvreader)
    for row in csvreader:
        #Addiing to vote counter for each row
        total_vote += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            votes.append(1)
        else:
            index= candidates.index(row[2])
            votes[index]+= 1
# Calculating percentage vote
    for vote in votes:
        Percentvote = (vote / total_vote)
        Percentvote = "{:.3%}".format(Percentvote)
        Percent_votes.append(Percentvote)
# Results 
    winner = max(votes)
    winner_index= votes.index(winner)
    winner_name = candidates[winner_index]
# Printing the result
    print("Election Results")
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')
    print(f"Total Votes: {str(total_vote)}")
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')
    for i in range(len(candidates)):
         print(f"{candidates[i]}: {str(Percent_votes[i])} ({str(votes[i])})")
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')
    print(f"Winner : {str(winner_name)}")
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')
# Exporting text file
    output_path = os.path.join("analysis", "ElectionResult.txt")
    with open(output_path, 'w') as file:
        file.write("Election Results\n"
                  "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n"
                  f"Total Votes: {str(total_vote)}\n"
                  "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n")
        for i in range(len(candidates)):
            file.write(f"{candidates[i]}: {str(Percent_votes[i])} ({str(votes[i])})\n")
        file.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n"
                  f"Winner : {str(winner_name)}\n"
                  "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
file.close()    
