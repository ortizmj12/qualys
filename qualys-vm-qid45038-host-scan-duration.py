#!/usr/bin/env python

'''
Author: Michael Ortiz
Date: 2016-02-16
Last Modified: 2016-02-16

Script to parse the duration for each host scanned from the XML report.

Usage:
    ./qualys-qid45038.py <xml_file>
'''

import xml.etree.ElementTree as ET
import sys

xmlFile = sys.argv[1]
tree = ET.parse(xmlFile)
root = tree.getroot()

for asset in root.findall('IP'):
    ip = asset.get('value')
    result = asset.findall("./INFOS/CAT/INFO/[@number='45038']/RESULT")
    for times in result:
        duration = times.text.split("Scan duration: ")[1].split("seconds")[0]
        print ip + ", " + duration
