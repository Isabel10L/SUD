# copyFilesFromSubfolders
# Author:   Ivanov
# Revision: 0.2
#

import os
import shutil


def scanFolder(source, target):
    """ Scans a sourcefolder for csv-files and copies them to target.
        Returns number of files copied."""
    
    numberOfFilesCopied = 0
    
    for content in os.scandir(source):
        if content.is_dir():
            print(content.path)
            numberOfFilesCopied += scanFolder(content.path, target)
        elif content.is_file():
            if content.path.endswith(".csv"):
                print(content.path)
                shutil.copy(content, target)
                numberOfFilesCopied += 1

    return numberOfFilesCopied
                



# configuration
path = ".\\"
sourceFolderName = path + "quellordner\\"
targetFolderName = path + "zielordner\\"


# action
resultNumber = scanFolder(sourceFolderName, targetFolderName)
print(f"Anzahl kopierter Dateien:{resultNumber}")




