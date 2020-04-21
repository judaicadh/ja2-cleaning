from collections import defaultdict
import csv

reader = csv.reader(open('index-headers.csv'))

input_dict = {}
for row in reader:
    key = row[0]
    if key in result:
        # implement your duplicate row handling here
        pass
    result[key] = row[1:]
print(input_dict)

output_dict = defaultdict(list)

for k, v in input_dict.items():
    for e in v:
        output_dict[e].append(k)

with open('index-pids.csv', 'wb') as f:
    w = csv.DictWriter(f, output_dict.keys())
    w.writeheader()
    w.writerow(output_dict)