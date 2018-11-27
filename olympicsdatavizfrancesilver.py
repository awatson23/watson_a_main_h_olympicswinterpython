import csv
import numpy as np
import matplotlib.pyplot as plt

sex = []
Men = 0
Women = 0

with open("C:\\Users\\acade\\Desktop\\watson_a_main_h_olympicswinterpython\\data\\winterolympicsfrancesilver.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	line_count = 0
	for row in reader:
		if line_count is 0: # strip the headers out
			#categories.append(row)
			line_count += 1
		else:
			# collect the ratings info
			sex.append(row[2])
		
		line_count +=1

print("Starting second phase")
	
for item in sex: 
	if item == "Men":
		Men += 1

	else:
		Women += 1

total = Men + Women

men_percentage = (Men / total) * 100

women_percentage = (Women / total) * 100

gender = set(sex)

percents = [men_percentage, women_percentage]
gender = list(gender)
y_pos = np.arange(len(gender))

plt.bar(y_pos, percents)
plt.xticks(y_pos, gender)
plt.show()