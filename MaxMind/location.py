#!/usr/bin/env python

class Location(object):
	def __init__(self,
		geoname_id,
		locale_code = None,
		continent_code = None,
		continent_name = None,
		country_iso_code = None,
		country_name = None,
		subdivision_1_iso_code = None,
		subdivision_1_name = None,
		subdivision_2_iso_code = None,
		subdivision_2_name = None,
		city_name = None,
		metro_code = None,
		time_zone = None):
		self.geoname_id = geoname_id
		self.locale_code = locale_code
		self.continent_code = continent_code
		self.continent_name = continent_name
		self.country_iso_code = country_iso_code
		self.country_name = country_name
		self.subdivision_1_iso_code = subdivision_1_iso_code
		self.subdivision_1_name = subdivision_1_name
		self.subdivision_2_iso_code = subdivision_2_iso_code
		self.subdivision_2_name = subdivision_2_name
		self.city_name = city_name
		self.metro_code = metro_code
		self.time_zone = time_zone
	def __repr__(self):
		return str(self.geoname_id)
