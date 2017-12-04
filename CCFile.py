import os
import os.path


class CCFile:

    # Replaces part of a file name for all files in a directory
    # https://stackoverflow.com/questions/225735/batch-renaming-of-files-in-a-directory
    def replaceFileNames(self, find, replace, dir):
        for f in os.listdir(dir):
            if not f.startswith('.'):
                oldfile = dir + "\\" + f
                newfile = dir + "\\" + f.replace(find, replace)
                os.rename(oldfile, newfile)

    def getCurrentPath(self, filepath):
        curfilePath = os.path.abspath(filepath)
        # this will return current directory in which python file resides.
        curDir = os.path.abspath(os.path.join(curfilePath, os.pardir))
        return curDir

    def getParentPath(self, filepath):
        # this will return parent directory.
        parentDir = os.path.abspath(os.path.join(self.getCurrentPath(filepath), os.pardir))
        return parentDir

    def getCurrentDir(self, filepath):
        curfilePath = os.path.abspath(filepath)
        # this will return current directory in which python file resides.
        curDir = os.path.basename(curfilePath)
        return curDir

    def getParentCir(self, filepath):
        # this will return parent directory.
        parentPath = os.path.abspath(os.path.join(self.getCurrentPath(filepath), os.pardir))
        parentDir = os.path.basename(parentPath)
        return parentDir
