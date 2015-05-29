#!/usr/bin/env python

from __future__ import print_function
from MaxMind import reader
from MaxMind import block

class BlockReader(reader.Reader):
	def __init__(self, filename):
		super(BlockReader, self).__init__(filename)
	def read(self):
		blocks = []
		for b in self._read():
			blocks.append(block.Block(**b))
		return blocks
