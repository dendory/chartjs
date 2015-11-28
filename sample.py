import chartjs
import csv

# Create a new chart object and set some values
mychart = chartjs.chart("Wind energy visualization (in million KW/h) for 2010-2012", "Line", 1600, 800)

# Set some basic options
mychart.set_params(barValueSpacing = 100)

# Labels will be countries
countries = []

# We will make 3 datasets for the last 3 years available in our CSV file
values2012 = []
values2011 = []
values2010 = []
value = {'2010': 0, '2011': 0, '2012': 0}

# Read data from sample.csv
f = open("sample.csv", 'r', newline='')
data = csv.reader(f, delimiter=',')
next(data) # Skip headers

# Iterate through the file, then add datasets every time the country name changes
for line in data:
	if len(line) > 4 and float(line[4]) > 100:
		if line[0] not in countries:
			# Place the values of the last country in our lists
			if countries != []:
				values2012.append(value['2012'])
				values2011.append(value['2011'])
				values2010.append(value['2010'])
			# Reset values for the next country
			for k,v in value.items():
				value[k] = 0
			# Append this country to the list of labels
			countries.append(line[0])
		# Check the three years we care about
		if line[2] in value.keys():
			value[line[2]] = float(line[4])
# Add the last country in the list
values2012.append(value['2012'])
values2011.append(value['2011'])
values2010.append(value['2010'])

# Set labels to be the countries found in our file
mychart.set_labels(countries)

# Add three datasets for the three years
mychart.add_dataset(values2012)
mychart.set_params(fillColor = "rgba(100,200,200,0.25)", strokeColor = "rgba(100,200,200,0.75)", pointColor = "rgba(100,200,200,0.75)")
mychart.add_dataset(values2011)
mychart.set_params(fillColor = "rgba(200,100,100,0.25)", strokeColor = "rgba(200,100,100,0.75)", pointColor = "rgba(200,100,100,0.75)")
mychart.add_dataset(values2010)

# Close CSV file
f.close()

# Write sample.html
f = open("sample.html", 'w')
f.write(mychart.make_chart_full_html())
f.close()
