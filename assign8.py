#15-1 Cubes
from matplotlib import pyplot as plt

xValues = list(range(5001))
cubes = [x**3 for x in xValues]

plt.scatter(xValues, cubes, edgecolor = 'none', s = 40)

plt.title("15-1 Cubes", fontsize = 22)
plt.xlabel('Value', fontsize = 12)
plt.ylabel('Cube Value', fontsize = 12)
plt.tick_params(axis = 'both', labelsize = 12)
plt.axis([0, 5100, 0, 5100**3])

plt.show()

#15-2 Colored Cubes
from matplotlib import pyplot as plt

xValues = list(range(5001))
cubes = [x**3 for x in xValues]

plt.scatter(x_values, cubes, edgecolor='none', c=cubes, cmap=plt.cm.BuGn, s=40)

plt.title("15-1 Cubes", fontsize = 22)
plt.xlabel('Value', fontsize = 12)
plt.ylabel('Cube Value', fontsize = 12)
plt.tick_params(axis = 'both', labelsize = 12)
plt.axis([0, 5100, 0, 5100**3])

plt.show()

#15-3 Molecular Motion
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.figure(dpi = 128, figsize = (10, 6))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth = 1)
    plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 75)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 75)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    
    keep_running = input("Would you like to make another walk? (Y/N): ")
    if keep_running == 'n' or 'N':
        break
		
#15-4 Modified Ramdon Walks
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.figure(dpi = 128, figsize = (10, 6))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth = 1, zorder = 1)
    plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 75, zorder = 2)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 75, zorder = 2)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    
    keep_running = input("Would you like to make another walk? (Y/N): ")
    if keep_running == 'n' or 'N':
        break

#15-5 Refactoring 
class RandomWalk():
    
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            
            if x_step == 0 and y_step == 0:
                continue
            
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

#16-1 San Fransisco
import csv
from datetime import datetime

from matplotlib import pyplot as plt

fileName = 'sitka_weather_07-2014.csv'
with open(fileName) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], "%Y-%M-%D")
			#dates.append(current_date)
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c = 'red', alpa = .5)
plt.plot(dates, lows, c = 'blue', alpha = .5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = .1)

tableTitle = "Daily high and low temps Sitka"
#title += "secondary title..."
plt.title(tableTitle, fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.ylim(10, 120)

plt.show()

#16-2 Sitka-Death Valley Comparison 
	##adjusted above code, see commented out lines
	
#16-3 Rainfall
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_rainfall_2015.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfalls = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rainfall = float(row[19])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)

fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, rainfalls, c = 'blue', alpha = .5)
plt.fill_between(dates, rainfalls, facecolor = 'blue', alpha = .2)

title = "Daily rainfall amounts "
plt.title(title, fontsize = 20)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (inches)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()

#16-4 Explore 

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_rainfall_2015.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfalls, totals = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rainfall = float(row[19])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)
            if totals:
                totals.append(totals[-1] + rainfall)
            else:
                totals.append(rainfall)

fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, rainfalls, c = 'blue', alpha = .5)
plt.fill_between(dates, rainfalls, facecolor = 'blue', alpha = .2)

plt.plot(dates, totals, c = 'blue', alpha = .75)
plt.fill_between(dates, totals, facecolor = 'blue', alpha = .05)

title = "Daily rainfall amounts and cumulative rainfall "
plt.title(title, fontsize = 20)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (inches)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()