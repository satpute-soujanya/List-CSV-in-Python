import os
import csv
firm_name_Airtable = []

firm_name_sheet = []
with open('Firms-Main View.csv', 'r') as f:
    lines = f.readlines()
    for line in lines[1:]: # skip the first line (header)
        items = line.strip().split(',')
        firm_name = items[0]
        firm_name_Airtable.append(firm_name)
        # print(firm_name_Airtable)


print(len(firm_name_Airtable))
with open('Funds below $200M in Size - $200M fund data.csv', 'r') as f:
    lines = f.readlines()
    for line in lines[1:]: # skip the first line (header)
        items = line.strip().split(',')
        firm_name = items[1]
        firm_name_sheet.append(firm_name)

        # print(firm_name_sheet)
print(len(firm_name_sheet))


common_elements = set(firm_name_Airtable) & set(firm_name_sheet)
print(len(common_elements))
# print(common_elements)



inputfile = 'Firms-Main View.csv'
outputfile = 'common_firms.csv'
item_names = common_elements
with open(inputfile, "r") as input_csv_file, \
     open(outputfile, "w") as output_csv_file:
    csv_reader = csv.reader(input_csv_file)
    csv_writer = csv.writer(output_csv_file)
    header_row = next(csv_reader)
    csv_writer.writerow(header_row)
    for row in csv_reader:
            for item_name in item_names:
                print(row)
                if item_name in row:
                    csv_writer.writerow(row)
