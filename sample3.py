# This script parses the CSV files gathered from the Canadian Weather Service and makes charts
import chartjs
import csv

# We will cover these years
startyear = 1981
endyear = 2012

# We will make charts for 3 major Canadian cities
cities = [
	{'name': "Montreal", 'fillColor': "rgba(100,50,200,0.25)", 'strokeColor': "rgba(100,50,200,0.75)", 'pointColor': "rgba(100,50,200,0.75)"},
	{'name': "Toronto", 'fillColor': "rgba(200,100,100,0.25)", 'strokeColor': "rgba(200,100,100,0.75)", 'pointColor': "rgba(200,100,100,0.75)"},
	{'name': "Vancouver", 'fillColor': "rgba(100,200,100,0.25)", 'strokeColor': "rgba(100,200,100,0.75)", 'pointColor': "rgba(100,200,100,0.75)"},
]

# 3 of the charts will cover all 12 months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# The first chart will show median temperatures over the years
global_chart = chartjs.chart("Temperature medians for 1981 - 2012 in Celsius<br><font color='#6432C8'>Montreal</font>, <font color='#B1846B'>Toronto</font>, <font color='#6CCB6C'>Vancouver</font>", "Line", 1200, 600)
global_chart.set_params(JSinline = False)

# Each city will have a chart showing each month's median temperature
montreal_chart = chartjs.chart("Montreal temperatures for 2012 in Celsius", "Line", 390, 200)
montreal_chart.canvas = "montreal"
montreal_chart.set_labels(months)
toronto_chart = chartjs.chart("Toronto temperatures for 2012 in Celsius", "Line", 390, 200)
toronto_chart.canvas = "toronto"
toronto_chart.set_labels(months)
vancouver_chart = chartjs.chart("Vancouver temperatures for 2012 in Celsius", "Line", 390, 200)
vancouver_chart.canvas = "vancouver"
vancouver_chart.set_labels(months)

_startyear = startyear
# Loop one city at a time
for city in cities:
	city_data = []
	years = []
	medians = []
	# Loop one year at a time
	while startyear < endyear+1:
		# Open CSV file for the city and year
		f = open("data/" + city['name'] + "/" + str(startyear) + ".csv", 'r', newline='')
		next(f)
		csvreader = csv.reader(f, delimiter=',')
		totalvalues = 0
		values = 0
		monthly_values = 0
		monthly_totalvalues = 0
		current_month = '01'
		# Parse the CSV line by line
		for line in csvreader:
			try:
				# For each line, we add the value and the number of values
				values += float(line[9])
				totalvalues += 1
			except:
				pass
			try:
				# For year 2012, we also record monthly medians for the city charts
				if startyear == 2012:
					# If the month column changed, that means we must compute the median for last month
					if str(line[2]) != str(current_month):
						# All the added values, divided by the number of values
						median = "{0:.2f}".format(float(monthly_values / monthly_totalvalues))
						# Append the median to the current city's list
						city_data.append(median)
						# Set the current month to the new value
						current_month = str(line[2])
						# Reset variables to 0
						monthly_values = 0
						monthly_totalvalues = 0
					# For each line in this month, add the value and add the number of values
					monthly_values += float(line[9])
					monthly_totalvalues += 1					
			except:
				pass
		# For the last month, we need to calculate the median one last time
		if monthly_totalvalues > 0:
			median = "{0:.2f}".format(float(monthly_values / monthly_totalvalues))
			city_data.append(median)
		# After reading all the lines in the file, calculate the median for the year
		if totalvalues > 0:
			median = "{0:.2f}".format(float(values / totalvalues))
			medians.append(median)
		else:
			medians.append(0)
		# Append the current year to the labels
		years.append(startyear)
		# Create all of the city charts
		if startyear == 2012:
			if city['name'] == "Montreal":
				montreal_chart.set_params(fillColor = city['fillColor'], strokeColor = city['strokeColor'], pointColor = city['pointColor'])
				montreal_chart.add_dataset(city_data)
			if city['name'] == "Toronto":
				toronto_chart.set_params(fillColor = city['fillColor'], strokeColor = city['strokeColor'], pointColor = city['pointColor'])
				toronto_chart.add_dataset(city_data)
			if city['name'] == "Vancouver":
				vancouver_chart.set_params(fillColor = city['fillColor'], strokeColor = city['strokeColor'], pointColor = city['pointColor'])
				vancouver_chart.add_dataset(city_data)
		startyear += 1
	# Create the global chart
	global_chart.set_labels(years)
	global_chart.set_params(fillColor = city['fillColor'], strokeColor = city['strokeColor'], pointColor = city['pointColor'])
	global_chart.add_dataset(medians)
	startyear = _startyear
	f.close()

# Create the HTML page and the 4 charts individually
f = open("sample3.html", 'w')
output = """<!doctype html>
<html>
	<head>
		<title>Temperature charts</title>
		{1}
	</head>
	<body>
		<div style="width: {2}px; height: {3}px; max-width: 99%" class="chartjs">
			<center><h2>{0}</h2></center>
""".format(global_chart.title, global_chart.js, str(global_chart.width), str(global_chart.height))
output += global_chart.make_chart_canvas()
output += "			<table width='99%'><tr><td><center><h4>" + montreal_chart.title + "</h4></center>"
output += montreal_chart.make_chart_canvas()
output += "			</td><td><center><h4>" + toronto_chart.title + "</h4></center>"
output += toronto_chart.make_chart_canvas()
output += "			</td><td><center><h4>" + vancouver_chart.title + "</h4></center>"
output += vancouver_chart.make_chart_canvas()
output += """			</td></tr></table>
			<script>
				window.onload = function()
				{"""
output += global_chart.make_chart_onload()
output += montreal_chart.make_chart_onload()
output += toronto_chart.make_chart_onload()
output += vancouver_chart.make_chart_onload()
output += """				}
			</script>
		</div>
	</body>
</html>
"""
f.write(output)
f.close()
