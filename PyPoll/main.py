import csv
from collections import Counter

file_path = "/Users/owner/OneDrive/python-challenge-main/PyPoll/Resources/election_data.csv"

with open(file_path, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    
    next(csvreader)
    total_votes = 0
    candidate_votes = Counter()

    # Iterate through rows
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Count votes for each candidate
        candidate_votes[row[2]] += 1

 # total Votes
print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)

# A complete list of candidates who received votes

print("Candidates who received votes:")
for candidate in candidate_votes.keys():
    print(candidate)

print("-" * 30)

# Print the percentage of votes each candidate won
print("Percentage of votes each candidate won:")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-" * 30)


# Print the total number of votes each candidate won
print("Total votes each candidate won:")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes}")

print("-" * 30)

# Determine the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print the winner
print(f"Winner: {winner} with {candidate_votes[winner]} votes")
print("-" * 30)
