import csv
import numpy as np
import matplotlib.pyplot as plt

biathlon = []
skating = []
skiing = []
bobsleigh = []
curling = []


with open("C:\\Users\\acade\\Desktop\\watson_a_main_h_olympicswinterpython\\data\\winterolympicsfrancetotal.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	line_count = 0
	
	for row in reader:
		if line_count is 0: # strip the headers out
			#categories.append(row)
			line_count += 1
		else:
			if row[5] == "Biathlon":
				biathlon.append(row[5])
			elif row[5] == "Curling":
				curling.append(row[5])
			elif row[5] == "Skating":
				skating.append(row[5])
			elif row[5] == "Skiing":
				skiing.append(row[5])
			else:
				bobsleigh.append(row[5])	

		line_count += 1
		
print("processed", line_count, "rows of data")
print("biathlon plays:", len(biathlon))
print("skating:", len(skating))
print("skiing:", len(skiing))
print("bobsleigh:", len(bobsleigh))
print("curling:", len(curling))	

pct_biathlon = len(biathlon) / line_count * 100
pct_skating = len(skating) / line_count * 100
pct_skiing = len(skiing) / line_count * 100
pct_bobsleigh = len(bobsleigh) / line_count * 100
pct_curling = len(curling) / line_count * 100
	
labels = 'Biathlon', 'Skating', 'Skiing', 'Bobsleigh', 'Curling'
sizes = [pct_biathlon, pct_skating, pct_skiing, pct_bobsleigh, pct_curling]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
explode = (0.1, 0, 0, 0, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True)
startangle=140
plt.axis('equal')

plt.legend(labels)
plt.title("Sports played by France in the olympics")
plt.show()
