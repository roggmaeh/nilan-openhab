#!/usr/bin/env python3
# -*- coding: ISO-8859-1 -*-
import os, sys
import csv

celsius = chr(176) + "C"

with open('nilan_modbus.csv', encoding='utf8') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',')
	for row in reader:
		#print(row['Unit'] + " " + celsius)
		if row['Unit'] == "text" or row['Unit'] == "ascii":
			print("String\t%s\t\t\"%s [%ss]\" (NILAN)" % (row['Name'], row['Description'], chr(37)))
		elif row['Unit'] == "%":	
			print("Number\t%s\t\t\"%s [%s.1f] %s\" (NILAN)" % (row['Name'], row['Description'], chr(37), chr(37)))
		elif row['Unit'] == celsius:
			print("Number\t%s\t\t\"%s [%s.1f] %sC\" <temperature> (NILAN)" % (row['Name'], row['Description'], chr(37), chr(176)))
		else:
			print("Number\t%s\t\t\"%s [%sd]\" (NILAN)" % (row['Name'], row['Description'], chr(37)))
