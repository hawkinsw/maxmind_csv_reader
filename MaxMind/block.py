#!/usr/bin/env python
from __future__ import print_function

class Block(object):
	def __init__(self, 
		network,
		geoname_id,
		registered_country_geoname_id = None,
		represented_country_geoname_id = None,
		is_anonymous_proxy = None,
		is_satellite_provider = None,
		postal_code = None,
		latitude = None,
		longitude = None):
		self.network = network 
		self.geoname_id = geoname_id 
		self.registered_country_geoname_id = registered_country_geoname_id 
		self.represented_country_geoname_id = represented_country_geoname_id 
		self.is_anonymous_proxy = is_anonymous_proxy 
		self.is_satellite_provider = is_satellite_provider 
		self.postal_code = postal_code 
		self.latitude = latitude 
		self.longitude = longitude 
	def __repr__(self):
		return ("%s: %s" % (str(self.network), str(self.geoname_id)))
