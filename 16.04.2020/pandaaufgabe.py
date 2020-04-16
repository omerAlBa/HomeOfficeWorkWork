import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
model = LinearRegression()

csv_data = pandas.read_csv("baby.csv")
csv_data_names = csv_data['name']
list_anna = csv_data[csv_data['name'] == 'Anna']
list_country_CA = list_anna[list_anna['state'] == 'CA']
list_gender = list_country_CA[list_country_CA['sex'] == 'girl']
listEnd_anna = list_gender.sort_values('year')

xs = [[x] for x in listEnd_anna['year']]
ys = listEnd_anna['number']
pre = model.fit(xs,ys)
pre2 = model.predict(xs)
print(pre2)

plt.plot(listEnd_anna['year'],listEnd_anna['number'])
plt.plot(listEnd_anna['year'], pre2)
plt.show()