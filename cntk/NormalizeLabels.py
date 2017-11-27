# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# author: janpos@microsoft.com
# ==============================================================================

import os
import string
from constants import Constants
from path_helper import *

imgDir = "C:/Users/pospa/Temp/aaa/ey"

const = Constants()

imgFilenames = getFilesInDirectoryByType(imgDir, ["jpg","png"])
for imgIndex, imgFilename in enumerate(imgFilenames):
    print (imgIndex, imgFilename)
    labelsPath = os.path.join(imgDir, imgFilename[:-4] + ".bboxes.labels.tsv")
    if not os.path.exists(labelsPath):
        print ("Skipping image {:3} ({}) since annotation file doesn't exists: {}".format(imgIndex, imgFilename, labelsPath))
        continue
    labels = readFile(labelsPath)
    print(labels)
    oldLabels = const.getObsoleteCzechCharactersOnly()
    for character in list(oldLabels):
        labels = [const.getNationalCharacterAlternative(c)
            if c==character else c for c in labels]
    print(labels)
    for index, item in enumerate(labels):
        labels[index] = item.decode('utf-8')
    print(labels)
    #print (lambda label: label.decode('utf-8'), labels)
    writeFile(labelsPath, labels)