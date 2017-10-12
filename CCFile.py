import os


class CCFile:

    # Replaces part of a file name for all files in a directory
    # https://stackoverflow.com/questions/225735/batch-renaming-of-files-in-a-directory
    def replaceFileNames(self, find, replace, dir):
        for f in os.listdir(dir):
            if not f.startswith('.'):
                oldfile = dir + "\\" + f
                newfile = dir + "\\" + f.replace(find, replace)
                os.rename(oldfile, newfile)
