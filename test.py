import csv

my_dict = {}
with open('ja-index-revised.txt', 'r') as file_object:
    for values in file_object:
        values = values.split(",")
        key = next(file_object, None)
        if key is None:
            # oops, we got to the end of the file early
            raise ValueError('Invalid file format, missing key')
        my_dict[key.strip()] = values
print(my_dict)
#file = open('newfile.txt')
#file.write(data2)
    #entry = {}
    #for x in data2:
    #        key, value = x.split("Copies:")
    #        entry[key] = x.split([1])
    #file = open("newfile.txt", "a+")
    #file = open('supp.txt').read()

with open('new.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['copies', 'entry'])
    for biblio in my_dict:
        writer.writerow([biblio, ] + [i for i in my_dict[biblio]]) #not entirely clear of what this line does?
