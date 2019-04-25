#!/usr/bin/env python

'''
Author: Michael Ortiz
Date: 2016-05-24
Last Modified: 2016-05-25

Script to parse the duration of scan times from HTML reports.

Usage:
    ./qualys-was-scan-diagnostics.py <file>
'''

import sys

testResults = []

#Open file and puts lines into a list
file = sys.argv[1]
with open(file, 'r') as html:
    lines = html.readline().split("<br/>")

#Get the average server response time
for item in lines:
    if "Average server response time" in item:
        print item

#Create list of test results
for item in lines:
    if "Batch" in item and "seconds" in item:
        testResults.append(item)

#Parse out the goods
for test in testResults:
    '''
    testName = test.split(":")[0]
    testDetails = test.split(":")[1]
    numOfTests = testDetails.split(",")[0]
    secsPerTest = testDetails.split(",")[2].split(".")[0]
    if int(secsPerTest.split(" ")[1]) > 300:
        print testName+','+ numOfTests+','+secsPerTest+' *****'
    else:
        print testName+','+ numOfTests+','+secsPerTest
    '''
    print test.split('.')[0]
