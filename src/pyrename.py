import os
import sys

def main(folderlist):
    for folder in folderlist:
        print (folder)
        if os.path.exists(folder):
            for (path, dir, files) in os.walk(folder):
                for filename in files:
                    tf = os.path.join(path, filename)
                    pathStart = path.rfind('\\')
                    newFilename = path[pathStart+1:]+ "_" +filename
                    print(newFilename)
                    print(tf)
                    newTF = os.path.join(path, newFilename)
                    os.rename(tf, newTF)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("There is no folder name!\n")
    else:    
        main(sys.argv[1:])