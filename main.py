#!/usr/bin/env python

from __future__ import print_function
from MaxMind import block
from MaxMind import location
from MaxMind import blockreader
from MaxMind import locationreader

if __name__=="__main__":	
	b = block.Block("1.2.3.4/8", "9")
	l = location.Location(0)
	br = blockreader.BlockReader("GeoLite2-City-CSV_20150505/GeoLite2-City-Blocks-IPv4.csv")
	lr = locationreader.LocationReader("GeoLite2-City-CSV_20150505/GeoLite2-City-Locations-en.csv")
	print("b: " + str(b))
	print("l: " + str(l))
	print("br: " + str(br))
	#blocks = br.read()
	#print("Read %d blocks." % len(blocks))
	locations = lr.read()
	print("Read %d locations." % len(locations))
