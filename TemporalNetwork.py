#!/usr/bin/python

from Node import Node 
from Link import Link

FRONT_SEP = "--["
BACK_SEP = "]-->"


class TemporalNetwork:
	def __init__(self):
		self.nodes = []
		self.links = []
		self.fanOut = {}
		self.fanIn = {}

	def addNode(self, node):
		if node not in self.nodes:
			self.nodes.append(node)
			self.fanOut[node] = []
			self.fanIn[node] = []

	def addLink(self, link):
		if link not in self.links:
			self.addNode(link.n1)
			self.addNode(link.n2)
			self.links.append(link)
			self.fanOut[link.n1].append(link)
			self.fanIn[link.n2].append(link)


def readFile(filePtr):
	tn = TemporalNetwork()
	for line in filePtr:
		n1_name = line.split(FRONT_SEP)[0]
		n2_name = line.split(BACK_SEP)[1].rstrip('\n')
		c1 = line.find(FRONT_SEP) + len(FRONT_SEP)
		c2 = line.find(BACK_SEP)
		cons = float(line[c1:c2])
		if cons > 1000:
			cons = 10
		elif cons < 0:
			cons = 1
		node1 = Node(n1_name)
		node2 = Node(n2_name)
		link = Link(node1, node2, cons)
		tn.addLink(link)

	return tn