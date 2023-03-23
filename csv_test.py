import csv
import os

with open('metadata_of_corpus.csv', newline='') as in_file:
    with open ('try.csv', 'w', newline='') as out_file:
        csvreader = csv.reader(in_file)
        writer = csv.writer(out_file)
    for line in csvreader:
        if any(line):
            writer.(line)
print("complete")