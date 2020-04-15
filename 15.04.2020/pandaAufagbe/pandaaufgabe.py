import pandas

csv_data = pandas.read_csv("baby.csv")
csv_data_name_bool = csv_data['name'] == 'anna'
csv_data_name = csv_data['name'][csv_data_name_bool]
print(csv_data_name)