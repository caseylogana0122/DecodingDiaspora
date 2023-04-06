import csv
import os

filename = "metadata_of_corpus.csv"
rows = []

# Read the CSV file into a list
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = [row for row in csvreader]

# Delete the rows where two columns are empty
new_rows = []

for row in rows:
    if row[1] !="" and row[2] !="":
        new_rows.append(row)

# Write the modified list back to the CSV file
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(new_rows)
print("here!")