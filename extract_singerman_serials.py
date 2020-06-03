# -------------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------------
import csv
import pandas as pd

# -------------------------------------------------------------------------------
# Create a dictionary = 'singerman_number': (entry, copies, notes)
# -------------------------------------------------------------------------------
entry = {} # initialize dictionary
singerman_number = '' # keeping track of the current entry in the bibliography
text_file = open('serials-test.txt')
year = ""
for line in text_file:
    if line.strip(): #ignoring blank lines
        if line.strip().startswith("S0"):
            copy_start = False
            singerman_number = line.split()[0]
            entry[singerman_number] = [' '.join(line.split()[1:])]
        elif line.strip().startswith("S1"):
            copy_start = False
            singerman_number = line.split()[0]
            entry[singerman_number] = [' '.join(line.split()[1:])]
        elif line.strip().startswith("S2"):
            copy_start = False
            singerman_number = line.split()[0]
            entry[singerman_number] = [' '.join(line.split()[1:])]
        elif line.strip().startswith("S3"):
            copy_start = False
            singerman_number = line.split()[0]
            entry[singerman_number] = [' '.join(line.split()[1:])]
        elif line.strip().startswith("S4"):
            copy_start = False
            singerman_number = line.split()[0]
            entry[singerman_number] = [' '.join(line.split()[1:])]
        elif line.strip().startswith("S5"):
            copy_start = False
            singerman_number = line.split()[0]
            entry[singerman_number] = [' '.join(line.split()[1:])]
        elif line.strip().startswith("S6"):
            copy_start = False
            singerman_number = line.split()[0]
            entry[singerman_number] = [' '.join(line.split()[1:])]
        else:
            line = line.strip() # Remove leading/trailing spaces
            entry[singerman_number].append(line) # appends to line
print(entry)

# -------------------------------------------------------------------------------
# Write that dictionary to a csv
# -------------------------------------------------------------------------------
with open('singerman-serials.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['singerman_number','entry','notes','copies'])
    for biblio in entry:
        writer.writerow([biblio, ] + [i for i in entry[biblio]]) #not entirely clear of what this line does?
