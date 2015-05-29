#!/usr/bin/env python

from __future__ import print_function
from MaxMind import reader
from MaxMind import location

class LocationReader(reader.Reader):
	def __init__(self, filename):
		super(LocationReader, self).__init__(filename)
	def read(self):
		locations = []
		for l in self._read():
			print(l)
			locations.append(location.Location(**l))
		return locations
