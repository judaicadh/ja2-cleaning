# -------------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------------
import csv
from collections import defaultdict

# -------------------------------------------------------------------------------
# Open the existing CSV to create an input dictionary
# -------------------------------------------------------------------------------
reader = csv.reader(open('index-headers.csv'))

input_dict = {} # initialize dictionary 
for row in reader:
    key = row[0] # the key is the first part of the row
    if key in result:
        # implement your duplicate row handling here
        pass
    result[key] = row[1:] 
print(input_dict)

# -------------------------------------------------------------------------------
# Restructure the input dictionary for an output dictionary
# -------------------------------------------------------------------------------
output_dict = defaultdict(list)

for k, v in input_dict.items():
    for e in v:
        output_dict[e].append(k)

# -------------------------------------------------------------------------------
# Write the output dictionary to a csv
# -------------------------------------------------------------------------------
with open('index-pids.csv', 'wb') as f:
    w = csv.DictWriter(f, output_dict.keys())
    w.writeheader()
    w.writerow(output_dict)
