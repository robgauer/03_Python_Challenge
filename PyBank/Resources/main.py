' HEADER
# ^^^^^^ 
# Filename PyBank.py
# Python Version 3.6.10
# Creator Rob Gauer
#
#
' ASSIGNMENT INSTRUCTIONS
# ^^^^^^^^^^^^^^^^^^^^^^^ 
# PyBank
#
#	• In this challenge, you are tasked with creating a Python script for 
#   analyzing the financial records of your company. 
#   You will give a set of financial data called budget_data.csv. 
#   The dataset is composed of two columns: Date and Profit/Losses. 
#   (Thankfully, your company has rather lax standards for 
#   accounting so the records are simple.)
#	• Your task is to create a Python script that analyzes the records to
#   calculate each of the following:
#		○ The total number of months included in the dataset
#		○ The net total amount of "Profit/Losses" over the entire period
#		○ The average of the changes in "Profit/Losses" over the entire period
#		○ The greatest increase in profits (date and amount) over the entire period
#   	○ The greatest decrease in losses (date and amount) over the entire period
#	• As an example, your analysis should look similar to the one below:
#
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   In addition, your final script should both print the analysis to 
#   the terminal and export a text file with the results.
#
#
' PROGRAM CODE
# ^^^^^^^^^^^^
' IMPORT CSV FILE
#   Read dataset file called budget_data.csv. Import CSV file.
#   First we'll import the os module
#   This will allow us to create file paths across operating systems
import os

#   Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#   Method 1: Plain Reading of CSV files
#   with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

#   Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row) 
# 
#
' Calculate The total number of months included in the dataset
#
# 
' The net total amount of "Profit/Losses" over the entire period
' 
' The average of the changes in "Profit/Losses" over the entire period
' 
' The greatest increase in profits (date and amount) over the entire period
' 
' The greatest decrease in losses (date and amount) over the entire period 
' 