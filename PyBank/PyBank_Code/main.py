# -----------------------
# HEADER
# -----------------------
# Filename PyBank.py
# Python Version 3.6.10
# Creator Rob Gauer
#
# -----------------------
# ASSIGNMENT INSTRUCTIONS
# ----------------------- 
# PyBank
#
#	• In this challenge, you are tasked with creating a Python script for 
#   analyzing the financial records of your company. 
#   You will give a set of financial data called budget_data.csv. 
#   The dataset is composed of two columns: Date and Profit/Losses. 
#   (Thankfully, your company has rather lax standards for 
#   accounting so the records are simple.)
#	
#   Objective - Your task is to create a Python script that analyzes the records to
#   calculate each of the following:
#		A. The total number of months included in the dataset
#		B. The net total amount of "Profit/Losses" over the entire period
#		C. The average of the changes in "Profit/Losses" over the entire period
#		D. The greatest increase in profits (date and amount) over the entire period
#   	E. The greatest decrease in losses (date and amount) over the entire period
#	    F. As an example, your analysis should look similar to the one below:
#
#       Financial Analysis
#       ----------------------------
#       Total Months: 86
#       Total: $38382578
#       Average  Change: $-2315.12
#       Greatest Increase in Profits: Feb-2012 ($1926159)
#       Greatest Decrease in Profits: Sep-2013 ($-2196167)
#       In addition, your final script should both print the analysis to 
#       the terminal and export a text file with the results.
#
# -----------------------
# PROGRAM CODE
# -----------------------
#
# MODULES
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# _________________________________________________________
# VARIABLES
count_dates=0
profit_sum=0
profitloss_sum=0
profitloss_total=0
profit=0

# _________________________________________________________
# IMPORT FILE # Locate source data path location
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# print(csvpath) # displays file path to terminal

#
# CREATE LISTS
profit_min=[]
profit_max=[]
profit=[]
profit_loss=[]
date=[]
    
#
# _________________________________________________________
# READ FILE # Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader) # displays file data to terminal

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}") # displays file headers to terminal

    # _________________________________________________________
    # A. The total number of months included in the dataset
    # B. The net total amount of "Profit/Losses" over the entire period
    # Read each row of data after the header
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(row[1])
        # print(row) # displays file data to terminal
        count_dates=count_dates+1
        profit = int(row[1])
        if profit > 0:
            profit_sum = profit_sum + profit               
        elif profit < 0:
            profitloss_sum = profitloss_sum + profit
        profitloss_total = profitloss_sum + profit_sum
        #   print(f"Total: " + (profitloss_total))
        #   total profit loss
    
    # D. The greatest increase in profits (date and amount) over the entire period
    # E. The greatest decrease in losses (date and amount) over the entire period
    greatestinc=profit_loss[0]
    greatestdec=profit_loss[0]
    profit_total = 0
    for row in profit_loss:
        profit_total += int(row)
    
    # Greatest increase and decrease with month occurred
    # ---need to fix formulas---
    for row in range(len(profit_loss)):
        if profit_loss[row] >= greatestinc:
            greatestinc = profit_loss[row]
            greatestincmonth = date[row]
        elif profit_loss[row] <= greatestdec:
            greatestdec = profit_loss[row]
            greatestdecmonth = date[row]
    
    # C. The average of the changes in "Profit/Losses" over the entire period
        averagechange = round(profit_total / count_dates, 2)
   
# _________________________________________________________
# PRINT SUMMARY TO TERMINAL
print("")
print("")
print("Financial Analysis")
print("------------------------------------------------------")
print("Total Months .................. :                   " + str(count_dates))
#print("Profit Sum: " + str(profit_sum))
#print("Profit Loss Sum: " + str(profitloss_sum))
print("Profit and Loss Total ......... :             " + str(profitloss_total))
#print("Profit: " + str(profit))
#print("Greatest increase in profit: ", max(csvreader))
#print("Greatest decrease in profit: ", min(csvreader))
print("Average Revenue Change ........ :            "+ str(averagechange))
print("Greatest increase in profit ... : "+ str(greatestincmonth)+ " ($    "+ str(greatestinc)+ ")")
print("Greatest decrease in profit ... : "+ str(greatestdecmonth)+ " ($  "+ str(greatestdec)+ ")")
print("")
print("")
#
# _________________________________________________________
# OUTPUT TO FILE # Specify the file to write to
textoutput_path = os.path.join("..", "output", "pybank_output.txt")

# Open the output file using "write" mode. Specify the variable to hold the contents
with open(textoutput_path, 'w', newline='') as pybank:
    write = csv.writer(pybank)
    write.writerows([
        ["Financial Analysis"],
        ["---------------------------------------------------------"],
        ["Total Months .............................. :          " + str(count_dates)],
        ["Profit and Loss Total ..................... :    " + str(profitloss_total)],
        ["Average Revenue Change .................... :   "+ str(averagechange)],
        ["Greatest increase in profit .... :   "+ str(greatestincmonth)+ "  ($   "+ str(greatestinc)+ ")"],
        ["Greatest decrease in profit .... :   "+ str(greatestdecmonth)+ "  ($ "+ str(greatestdec)+ ")"]
    ])

# -----------------------
# EOF
# -----------------------

            





    