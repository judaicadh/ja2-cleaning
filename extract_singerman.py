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
text_file = open('test copy.txt')
year = ""
for line in text_file:
    if line.strip(): #ignoring blank lines
        if line.strip().isnumeric():
            year = line.strip()
        elif line.split()[0].isnumeric(): # Found a line with numbers, it's a new entry in the bibliography
            singerman_number = line.split()[0]
            entry[singerman_number] = [year, ' '.join(line.split()[1:])]
        else:
            line = line.strip() # Remove leading/trailing spaces
            entry[singerman_number].append(line) # appends to line
print(entry)

# -------------------------------------------------------------------------------
# Write that dictionary to a csv
# -------------------------------------------------------------------------------
with open('singerman-073019.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['singerman_number', 'year', 'details','notes','copies'])
    for biblio in entry:
        writer.writerow([biblio, ] + [i for i in entry[biblio]]) #not entirely clear of what this line does?

# -------------------------------------------------------------------------------
# Merge that CSV with existing CSVs for digital copies
# -------------------------------------------------------------------------------
#singerman_bibliography = pd.read_csv("test.csv")
#volume1 = pd.read_csv("Volume1.csv")
#singerman_bibliography_volume1 = singerman_bibliography.merge(volume1, on="singerman_number") #need to be sure to KEEP any singerman numbers from volume1 that DON'T have a duplicate in singerman_bibliography

#singerman_volume1 = pd.read_csv(singerman_bibliography_volume1)
#volume2 = pd.read_csv("Volume2.csv")
#singerman_final = singerman_volume1.merge(volume2, on="singerman_number")
