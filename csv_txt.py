import csv
import os

with open(r'CSV_Progress.csv') as f:
    with open('metadata_of_corpus.txt', 'w') as md:
        #column names
        md.write("dcterms:title,dcterms:date,dcterms:spacial")

        #skips first line in CSV
        next(f)

        for line in f:
            md.write("\n")
            newrow = "FN-" + line[0] + line[1] + "," + line[2] + "," + line[3]
            md.write(newrow)
    md.close()
f.close()
print("complete")