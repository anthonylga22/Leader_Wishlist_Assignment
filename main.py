import csv

text_conversion = {
    'Most desired (select only 1)':1,
    '2nd Most Desired (select only 1)':2,
    'Interested in leading (unlimited selections)':3,
    'Can lead if necessary (unlimited selections)':4,
    'Can\'t commit, not interested/able (unlimited selections)':5
}

dataset = []
curated_names = []
curated_votes = []

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            #print(row)
            #print("\n")
            dataset.append(row)

            #return dataset

file_path = 'data.csv'  ""
dataset_answers = read_csv_file(file_path)

#Changes the column name to the trip names
#Dataset[0]
replace_text = "Select only 1 trip from the 1st column and only 1 trip from 2nd column."
for i in range(len(dataset[0])):
    if replace_text in dataset[0][i]:
        broken_str = str(dataset[0][i]).split("[")
        broken_str_dash = broken_str[1].split("(")
        #print(broken_str_dash[0])
        curated_names.append(broken_str_dash[0])
    else: 
        curated_names.append(dataset[0][i])

#print(curated_names)

for i in range(3, len(dataset[1])):
    transfrom_txt = dataset[1][i]
    #print(text_conversion[transfrom_txt])
    curated_votes.append(text_conversion[transfrom_txt])

print(curated_names)
print(curated_votes)


final_list = []
for i in range(len(dataset)):
  if dataset[1][i] is 1:
      final_list.append(dataset[1][1])

