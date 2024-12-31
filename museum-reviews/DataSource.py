'''
Base class to be subclassed
'''

from openpyxl import load_workbook
import pandas as pd

class DataSource(object):
	def __init__(self, arg):
		super(DataSource, self).__init__()
		self.color = color			# '#70DCA6', '#4B81E9'
		self.name = name			# 'tripadvisor', 'googlemaps'
		self.seedUrl = seedUrl		# 'tripadvisor.com', 'maps.google.com'

	def writeExcel():
		# Conditional formatting
		'source', self.name
		'color', self.color