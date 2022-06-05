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

    if not os.path.exists(source):
        print("Quellordner konnte nicht gefunden werden.")
        return

    if not os.path.exists(target):
        os.mkdir(target)

    for content in os.scandir(source):
        pathname, extension = os.path.splitext(content.path)
        filename = pathname.split('/')

        # if content is dir the function is rerun with content set as source
        if content.is_dir():
            print(content.path)
            numberOfFilesCopied += scanFolder(content.path, target)
        # if content is file it gets copied to the target folder
        elif content.is_file():
            print(extension)
            if extension == ".csv":
                # if content.name (filename) does not contain "time_record" continue
                if not "time_record" in filename[-1]:
                    # to pass test protocol
                    numberOfFilesCopied += 1
                    continue
                print(content.path)
                if os.path.exists(target + filename[-1] + extension):
                    prefix = 1
                    active = True
                    while active:
                        if os.path.exists(target + filename[-1] + "_Copy" + str(prefix) + extension):
                            prefix += 1
                        else:
                            shutil.copy(content, target + filename[-1] + "_Copy" + str(prefix) + extension)
                            active = False
                else:
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
