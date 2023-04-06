import csv
import os

with open(r'CSV_Progress.csv') as f:
    with open('metadata_of_corpus.csv', 'w') as md:
        #column names
        md.write("dcterms:title,dcterms:spatial,dcterms:date")

        csvreader = csv.reader(f, delimiter=',')
        next(csvreader)
        for line in csvreader:
            md.write("\n")
            if line[2] != "":
                newrow = "FN-" + line[0] + line[1] + "," + "\"" + line[2] +  "\"" + "," + line[3]
            else:
                newrow = "FN-" + line[0] + line[1] + ","  + line[2] +  "," + line[3]
            md.write(newrow)
    md.close()
f.close()
print("complete")