import chartjs
import csv

# Create a new chart object and set some values
mychart = chartjs.chart(title = "Wind energy visualization")

# Read data from sample.csv
f = open("sample.csv", 'r', newline='')
data = csv.reader(f, delimiter=',')

# Get headers
headers = next(data)

mychart.set_labels(["test1", "test2", "test3"])

mychart.add_dataset([1,2,3])
mychart.set_params(fillColor = "rgba(220,220,220,0.5)", strokeColor = "rgba(220,220,220,0.8)", highlightFill = "rgba(220,220,220,0.75)", highlightStroke = "rgba(220,220,220,1)",)
mychart.add_dataset([3,1.2,3])

#for line in data:
#	print(str(line))

# Close CSV file
f.close()

# Write chart1.html
f = open("chart1.html", 'w')
f.write(mychart.make_chart_full_html())
f.close()
