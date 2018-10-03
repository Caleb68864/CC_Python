import csv
from venv import logger


class CSVWriter:
    def __init__(self, file, mode='a', newline='', delimiter='|', quotechar='', quoting=csv.QUOTE_NONE):
        self.csvwriter = None
        self.file = file
        self.mode = mode
        self.newline = newline
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.quoting = quoting
        self.rows = []

    def write(self):
        with open(self.file, self.mode, newline=self.newline, encoding="utf-8") as csvfile:
            self.csvwriter = csv.writer(csvfile, delimiter=self.delimiter,
                                   quotechar=self.quotechar, quoting=self.quoting, escapechar='\\')
            for row in self.rows:
                try:
                    self.csvwriter.writerow(row)
                except Exception as e:
                    logger.error("Error: {}".format(str(e)))
                    logger.error(row)

    def addrow(self, row):
        self.rows.append(row)
