# -----------------------
# HEADER 
# -----------------------
# Filename PyPoll.py
# Python Version 3.6.10
# Creator Rob Gauer
#
# -----------------------
# ASSIGNMENT INSTRUCTIONS
# -----------------------  
# PyPoll
#
#	• In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
#   (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, 
#   his concentration is not what it used to be.)
#	• You will be give a set of poll data called election_data.csv. 
#   The dataset is composed of three columns: Voter ID, County, and Candidate. 
#   Your task is to create a Python script that analyzes the votes and calculates each of the following:
#		A. The total number of votes cast
#		B. A complete list of candidates who received votes
#		C. The percentage of votes each candidate won
#		D. The total number of votes each candidate won
#		E. The winner of the election based on popular vote.
#       F. In addition, your final script should both print the analysis to the terminal and 
#           export a text file with the results.
#	
#           As an example, your analysis should look similar to the one below:
#
#           Election Results
#           -------------------------
#           Total Votes: 3521001
#           -------------------------
#           Khan: 63.000% (2218231)
#           Correy: 20.000% (704200)
#           Li: 14.000% (492940)
#           OTooley: 3.000% (105630)
#           -------------------------
#           Winner: Khan
#           -------------------------
#
# -----------------------
# PROGRAM CODE
# -----------------------
# _________________________________________________________
# IMPORT CSV FILE
#   Read dataset file called election_data.csv. Import CSV file.
#   First we'll import the os module. This will allow us to create file paths across operating systems
import os
#   Module for reading CSV files
import csv

# _________________________________________________________
# IMPORT FILE # Locate source data path location
PyPollcsv = os.path.join("Resources","election_data.csv")

# _________________________________________________________
# VARIABLES and LISTS
total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = ""
dashsterminal = "     ------------------------------"
dashs = "  ----------------------------------"

# _________________________________________________________
# IMPORT FILE # Open csv file
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # _________________________________________________________ 
    # A. The total number of votes cast
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

# _________________________________________________________
# B. A complete list of candidates who received votes
# C. The percentage of votes each candidate won
# D. The total number of votes each candidate won
# E. The winner of the election based on popular vote.
# calculate vote percentage and identify winner
for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

# _________________________________________________________
# F. Final script should both print the analysis to the terminal 
# and export a text file with the results
# DISPLAY TO TERMINAL
print()
print()
print("     Election Results")
print(dashsterminal)
print(f"     Total Votes: {total_votes}")
print(dashsterminal)
for person, vote_count in candidate_votes.items():
    print(f"     {person}: {candidate_percentages[person]} ({vote_count})")
print(dashsterminal)
print(f"     Winner: {winner}")
print(dashsterminal)
print()
print()

# EXPORT to FILE  # export a text file with the results
textoutput_path = os.path.join("..", "Output", "election_results.txt")
with open('electrion_results.txt', 'w') as text:
    text.write("  Election Results\n")
    text.write(dashs + "\n")
    text.write(f"  Total Votes: {total_votes}" + "\n")
    text.write(dashs + "\n")
    for person, vote_count in candidate_votes.items():
        text.write(f"  {person}: {candidate_percentages[person]} ({vote_count})" + "\n")
    text.write(dashs + "\n")
    text.write(f"  Winner: {winner}" + "\n")
    text.write(dashs + "\n")

# ----------------------- 
# EOF
# -----------------------