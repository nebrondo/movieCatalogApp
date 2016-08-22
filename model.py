
import json
""" Class that defines the means to extract data, either from a local json file
    or from a web service """
class Model():
	def __init__(self):
		# Opening data json file for parsing using json module
		data = open("data.json")
		# json object associated with the data attribute
		self.data = json.load(data)