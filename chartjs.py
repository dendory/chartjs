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
		print()
	
	def make_chart_full_html(self):
		print()
		self.make_chart()
		print()

	def make_chart_with_headers(self):
		print("HTTP/1.0 200 OK")
		print("Content-Type: text/html; charset=utf-8")
		print()
		self.make_chart_full_html()
