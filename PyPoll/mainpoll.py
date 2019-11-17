import os
import csv
votescsv = os.path.join("/Users/danbishop/Desktop/","election_data.csv")

#Establish variables for candidate counts
total_votes = 0
candidates = []
Khan_count = 0
Correy_count = 0
Li_count = 0
OTooley_count = 0

#Open CSV, establish loops and run counts
with open(votescsv, newline= '') as data:
    csvreader = csv.reader(data, delimiter = ',')
    row = next(csvreader)
    
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = str(row[2])
        prev_candidate = str(row[2])
        if candidate != prev_candidate:
            candidates.append(candidate)
        elif candidate == prev_candidate:
            candidates.append(candidate)

#Calulating percentages, adding vote counts to each row in printed summary, and determining winner
with open(votescsv, newline= '') as data:
    csvreader = csv.reader(data, delimiter = ',')
    row = next(csvreader)
    for row in csvreader:
        if row[2] == "Khan":
            Khan_count +=1
        elif row[2] == "Correy":
            Correy_count += 1
        elif row[2] == "Li":
            Li_count += 1
        else:
            OTooley_count += 1
    
    khan_percent = Khan_count/total_votes
    correy_percent = Correy_count/total_votes
    li_percent = Li_count/total_votes
    otooley_percent = OTooley_count/total_votes

    winner = max(Khan_count,Correy_count,Li_count,OTooley_count)
    if winner == Khan_count:
        winningcand = "Khan"
    elif winner == Correy_count:
        winningcand = "Correy"
    elif winner == Li_count:
        winningcand == "Li"
    else:
        winningcand == "O'Toole"

#Print results
candidates = list(dict.fromkeys(candidates))
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
print(f"Khan: {khan_percent:.3%} ({str(Khan_count)})")
print(f"Correy: {correy_percent:.3%} ({str(Correy_count)})")
print(f"Li: {li_percent:.3%} ({str(Li_count)})")
print(f"O'Tooley: {otooley_percent:.3%} ({str(OTooley_count)})")
print("-------------------------")
print(f"Winner: {str(winningcand)}")
print("-------------------------")
print(candidates)

#Print results to txt file
output_poll = os.path.join("/Users/danbishop/Desktop/Rutgers Data Science Bootcamp/Python/python-challenge-db/PyPoll/", 'PyPoll.txt')
with open(output_poll, 'w',) as PyPoll:
    PyPoll.write("Election Results\n")
    PyPoll.write("-------------------------\n")
    PyPoll.write(f"Total Votes: {str(total_votes)}\n")
    PyPoll.write("-------------------------\n")
    PyPoll.write(f"Khan: {khan_percent:.3%} ({str(Khan_count)})\n")
    PyPoll.write(f"Correy: {correy_percent:.3%} ({str(Correy_count)})\n")
    PyPoll.write(f"Li: {li_percent:.3%} ({str(Li_count)})\n")
    PyPoll.write(f"O'Tooley: {otooley_percent:.3%} ({str(OTooley_count)})\n")
    PyPoll.write("-------------------------\n")
    PyPoll.write(f"Winner: {str(winningcand)}\n")
    PyPoll.write("-------------------------\n")