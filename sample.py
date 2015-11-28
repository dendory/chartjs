import chartjs
import csv

# Create a new chart object and set some values
mychart = chartjs.chart()
mychart.title = "Wind energy"

# Read data from sample.csv
f = open("sample.csv", 'r', newline='')
data = csv.reader(f, delimiter=',')

# Get headers
headers = next(data)

#for line in data:
#	print(str(line))

# Close CSV file
f.close()

# Write chart1.html
f = open("chart1.html", 'w')
f.write(mychart.make_chart_full_html())
f.close()
