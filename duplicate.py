import csv

filename = "metadata_of_corpus.csv"
rows = []

# Read the CSV file into a list
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

# Identify and delete exact duplicates
new_rows = []
existing_rows = set()

for row in rows:
    row_tuple = tuple(row)
    if row_tuple not in existing_rows:
        new_rows.append(row)
        existing_rows.add(row_tuple)

# Write the modified list back to the CSV file
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(new_rows)
print("here!")