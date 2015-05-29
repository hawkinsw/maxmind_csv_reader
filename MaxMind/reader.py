#!/usr/bin/env python

from __future__ import print_function

def smart_split(string, splitter):
	final_split = []
	temporary_split = []
	in_escape = False
	for f in string.split(splitter):
		if f.startswith("\"") and not f.endswith("\""):
			#Starting an escaped string.
			in_escape = True
		elif f.endswith("\"") and not f.startswith("\""):
			#Ending an escaped string.
			temporary_split.append(f)
			f = (splitter+" ").join(temporary_split)
			temporary_split = []
			in_escape = False

		if in_escape:
			temporary_split.append(f)
		else:
			final_split.append(f)
	return final_split

class Reader(object):
	def __init__(self, filename):
		self.filename = filename
	def __repr__(self):
		return self.filename
	def _read(self):
		blocks = []
		with open(self.filename, "r") as f: 
			header = []

			header_string = f.readline()
			for field in header_string.split(","):
				print("%s" % (field))
				header.append(field.rstrip())

			for line in f:
				entries = smart_split(line,",")
				entry = {}
				for index, field in zip(range(len(entries)), entries):
					entry[header[index]] = field.rstrip()
				yield entry
