#!/usr/bin/python

import getopt
import sys
import os
import time

n = len(sys.argv)

argumentList = sys.argv[1:]
options = "hf:o:n:"
long_options = ["help", "file=", "output=", "chunkSize="]
 
try:
    arguments, ueberhang = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print ("displaying help")
        if currentArgument in ("-f", "--file"):
            if os.path.exists(currentValue):
                with open(currentValue, "r") as file:
                    inputFile = file.read()
        if currentArgument in ("-o", "--output"):
            outputFileName = currentValue
        if currentArgument in ("-n", "--chunkSize"):
            chunkSize = int(currentValue)

    chunkSize = int(chunkSize) - 4
    inputLength = len(inputFile)
    chunks = []
    offset = 0
    i = 0

    while i <= inputLength:
        if i + chunkSize <= inputLength and inputFile[i + chunkSize] != " ":
            while inputFile[i + (chunkSize - offset)] != " ":
                offset += 1        
        chunks.append( inputFile[i:i + chunkSize - offset])
        i = i + chunkSize - offset
        offset = 0

    chunkCount = len(chunks)
    chunks[0] = str(1) + "/" + str(chunkCount) + " " + chunks[0]

    for k in range(1, chunkCount, 1):
        chunks[k] = str(k + 1) + "/" + str(chunkCount) + chunks[k]

    try: outputFileName
    except: outputFileName = "splitted_"

    outputFile = open(outputFileName + str(int(time.time())) + '.txt', 'a')

    for x in chunks:
        outputFile.write(x)
        outputFile.write('\n\n--------------------------------------\n\n')

except getopt.error as err:
    print (str(err))