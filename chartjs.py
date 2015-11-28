#
# Python ChartJS - (C) 2015 Patrick Lambert - Provided under the MIT License
# Uses the ChartJS JavaScript implementation by Nick Downie
#
import json

version = "0.1"

class chart:
	#
	# Utility functions
	#
	def __init__(self):
		self.title = "Untitled chart"
		self.data = []
		
	def _is_int(self, num): # Check if a number
		try:
			int(num)
			return True
		except ValueError:
			return False
	
	#
	# Main functions
	#
	def make_chart(self):
		output = ""
		return output
	
	def make_chart_full_html(self):
		output = """<!doctype html>
<html>
	<head>
		<title>{0}</title>
		<script src="chart.js"></script>
	</head>
	<body>
""".format(self.title)
		output += self.make_chart()
		output += """
	</body>
</html>
"""
		return output

	def make_chart_with_headers(self):
		output = ""
		output += "HTTP/1.0 200 OK\n"
		output += "Content-Type: text/html; charset=utf-8\n\n"
		output += self.make_chart_full_html()
		return output
