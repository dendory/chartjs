import chartjs
import csv

# Create a new chart object and set some values
mychart = chartjs.chart("Wind energy visualization (in million KW/h)", "Line", 1600, 800)

# Set some basic options
mychart.set_params(barValueSpacing = 100, scaleShowGridLines = False)

# Labels will be countries
countries = []

# We will make 3 datasets for the last 3 years available in our CSV file
values2012 = []
values2011 = []
values2010 = []

# Read data from sample.csv
f = open("sample.csv", 'r', newline='')
data = csv.reader(f, delimiter=',')
next(data) # Skip headers

# Iterate through the file, then add datasets every time the country name changes
for line in data:
	if len(line) > 4:
		if line[0] not in countries:
			if countries != []:
				values2012.append(value2012)
				values2011.append(value2011)
				values2010.append(value2010)
			# Reset values for the next country
			value2012 = 0
			value2011 = 0
			value2010 = 0
			# Append this country to the list
			countries.append(line[0])
		# Check the three years we care about
		if line[2] == '2012':
			value2012 = float(line[4])
		if line[2] == '2011':
			value2011 = float(line[4])
		if line[2] == '2010':
			value2010 = float(line[4])
# Add the last country in the list
values2012.append(value2012)
values2011.append(value2011)
values2010.append(value2010)

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
