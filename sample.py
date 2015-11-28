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

# Print the resulting full HTML page. We could also write it to a .html file
# or send the raw HTML to another framework using mychart.make_chart(), or use
# mychart.make_chart_with_headers() to also include the HTTP headers.
mychart.make_chart_full_html()
