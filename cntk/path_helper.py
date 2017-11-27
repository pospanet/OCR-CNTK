# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# author: janpos@microsoft.com
# ==============================================================================

import os

class UserDirectory:

    def getMissingLabelsImgageDir():
        print("Entering init UserDirectory")
        # Loged-in user
        windowsUser = os.getlogin()

        # Desktop folder
        desktop = os.path.join("C:/Users", windowsUser, "Desktop")

        # Path for Images and boxe
        imgDir = os.path.join("C:/Users", windowsUser, "Desktop/EY/dataset/missingLabels")
        if not os.path.isdir(imgDir):
            imgDir = os.path.join("C:/Users", windowsUser, "Projects/EY/dataset/missingLabels")
        return imgDir

    def getCroppedImgageDir():
        print("Entering init UserDirectory")
        # Loged-in user
        windowsUser = os.getlogin()

        # Desktop folder
        desktop = os.path.join("C:/Users", windowsUser, "Desktop")

        # Path for Images and boxe
        imgDir = os.path.join("C:/Users", windowsUser, "Desktop/EY/dataset/cropped")
        if not os.path.isdir(imgDir):
            imgDir = os.path.join("C:/Users", windowsUser, "Projects/EY/dataset/cropped")
        return imgDir

def getFilesInDirectory(directory, postfix = ""):
    fileNames = [s for s in os.listdir(directory) if not os.path.isdir(os.path.join(directory, s))]
    if not postfix or postfix == "":
        return fileNames
    else:
        return [s for s in fileNames if s.lower().endswith(postfix)]

def getFilesInDirectoryByType(directory, fileTypes):
    files = []
    for fileType in fileTypes:
        files += getFilesInDirectory(directory, "." + fileType)
    return files


####################################
# Functions
####################################


def readFile(inputFile):
    with open(inputFile,'rb') as f:
        lines = f.readlines()
    return [removeLineEndCharacters(s) for s in lines]



def readTable(inputFile, delimiter='\t', columnsToKeep=None):
    lines = readFile(inputFile)
    if columnsToKeep != None:
        header = lines[0].split(delimiter)
        columnsToKeepIndices = listFindItems(header, columnsToKeep)
    else:
        columnsToKeepIndices = None
    return splitStrings(lines, delimiter, columnsToKeepIndices)


def removeLineEndCharacters(line):
    if line.endswith(b'\r\n'):
        return line[:-2]
    elif line.endswith(b'\n'):
        return line[:-1]
    else:
        return line


def splitString(string, delimiter='\t', columnsToKeepIndices=None):
    if string == None:
        return None
    items = string.decode('utf-8').split(delimiter)
    if columnsToKeepIndices != None:
        items = getColumns([items], columnsToKeepIndices)
        items = items[0]
    return items

def splitStrings(strings, delimiter, columnsToKeepIndices=None):
    table = [splitString(string, delimiter, columnsToKeepIndices) for string in strings]
    return table

def writeFile(outputFile, lines):
    with open(outputFile,'w') as f:
        for line in lines:
            f.write("%s\n" % line)

def writeTable(outputFile, table):
    lines = tableToList1D(table)
    writeFile(outputFile, lines)


def tableToList1D(table, delimiter='\t'):
    return [delimiter.join([str(s) for s in row]) for row in table]