import csv

text_conversion = {
    'Most desired (select only 1)':1,
    '2nd Most Desired (select only 1)':2,
    'Interested in leading (unlimited selections)':3,
    'Can lead if necessary (unlimited selections)':4,
    'Can\'t commit, not interested/able (unlimited selections)':5
}

dataset = []
curated_data = [[]]

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dataset.append(row)


file_path = 'data.csv'
dataset_answers = read_csv_file(file_path)

#Changes the column name to the trip names
replace_text = "Select only 1 trip from the 1st column and only 1 trip from 2nd column."
for i in range(len(dataset[0])):
    if replace_text in dataset[0][i]:
        broken_str = str(dataset[0][i]).split("[")
        broken_str_dash = broken_str[1].split("(")
        #print(broken_str_dash[0])
        curated_data[0].append(broken_str_dash[0])
    else: 
        curated_data[0].append(dataset[0][i])

#Curates data
#Turns Most desired (Select only 1) into 1, etc
for i in range(1, len(dataset)):
    temp_lst = []
    for j in range(len(dataset[i])):
        transfrom_txt = dataset[i][j]
        if transfrom_txt in text_conversion:
            temp_lst.append(text_conversion[transfrom_txt])
        else:
            temp_lst.append(dataset[i][j])
            pass
    curated_data.append(temp_lst)


# print(curated_data)
# for i in range(len(curated_data)):
#    print(curated_data[i])

#Prints the trip name with the leaders
for k in range(3, len(curated_data[0])):
    print(curated_data[0][k])
    for i in range(1, 6) :
        print(f"Option {i}: ", end=" ")
        for j in range(len(curated_data)):
            if curated_data[j][k] == i:
                print((curated_data[j][1].split(" "))[0], end=", ")
        print("\n")
    print("\n")

