import csv
from collections import defaultdict
data_dict = defaultdict(list)
data_list = []

filename = "ja-index-10719.txt"
file = open(filename)
contents = file.read()
print(contents,"\n")
data_list = [lines.split(",") for lines in contents.split("\n")]
print(data_list)
for line in data_list:
    name = line[0:1]
    regNumber = line[1:]
    details = (name)
    data_dict[str(regNumber)].append(details)
    if not str(regNumber) in data_dict:
        data_dict[str(regNumber)] = list()
print(data_dict,"\n")
print(data_dict.items(),"\n")
print(data_dict.values())

with open("output.csv",'w') as f:
    writer = csv.writer(f)
    writer.writerows(data_dict.items())
