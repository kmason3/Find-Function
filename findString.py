#! /usr/bin/python

# Searches all the files in a directory for an instance of a user entered string
# If the string is found, the path the the file and line number is returned

import os
import sys

usage = '\nNAME\n \tfindString [path_to_directory] [string_to_find] \n\nSYNOPSIS\n\tSearches all files in a directory for the occurrence of entered string\n\n'
argLen = len(sys.argv)

if(argLen >= 3):
  
    directory = sys.argv[1]
    wordToFind = ' '.join(sys.argv[2:])

else:
    print(usage)
def searchDir(dirToSearch):

    if(os.path.isdir(dirToSearch)):
    
        for filename in os.listdir(dirToSearch):
    
            if (os.path.isfile(dirToSearch + '/' + filename)):
                findInFile(dirToSearch + '/' + filename, wordToFind)
    
            if (os.path.isdir(dirToSearch + '/' + filename)):
                searchDir(filename)

def findInFile(filePath, stringToFind):
    file = open(filePath, 'r')

    for num, line in enumerate(file,1):
        if(line.find(stringToFind) != -1):
            print("Found in " + filePath + '\nAt Line: ' + str(num) + '\n')
        
    file.close()

searchDir(directory)
    

