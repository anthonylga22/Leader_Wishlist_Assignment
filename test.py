import csv

test_dataset = []

with open("data1.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    test_dataset.append(row)

print(test_dataset)