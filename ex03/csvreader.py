# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/15 18:06:21 by archid-           #+#    #+#              #
#    Updated: 2023/04/18 08:46:13 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv
from pprint import pprint

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        if type(filename) != str:
            raise TypeError()
        if type(sep) != str:
            raise TypeError()
        if type(header) != bool:
            raise TypeError()
        if type(skip_top) != int:
            raise TypeError()
        if type(skip_bottom) != int:
            raise TypeError()
        if skip_bottom > skip_top:
            raise ValueError()
        self.file = open(filename, 'r')
        self.sep = sep
        if sep == '\"' or sep == '\'':
            raise ValueError()
        self.is_header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []
        self.header = []

    def __enter__(self):
        length = None
        for row in csv.reader(self.file, delimiter=self.sep):
            if length is None:
                length = len(row)
            elif length != len(row):
                raise ValueError()
            self.data.append(row)
        if self.is_header:
            self.header = self.data.pop(0)
        if self.skip_bottom != 0:
            self.data = self.data[self.skip_top:self.skip_bottom]
        else:
            self.data = self.data[self.skip_top:]
        return self

    def __exit__(self, *exc_details):
        self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        return self.data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        return self.header if self.is_header else None
    
def testReader(filename, sep, header, skip_top, skip_bottom):
    with CsvReader(filename, sep, header, skip_top, skip_bottom) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            # print('Header:', reader.getheader(), end = "\n")
            # print('Data  :', reader.getdata(), end = "\n\n")
            pprint(reader.getdata())

if __name__ == "__main__":
    testReader('good.csv', ',', False, 0, 0)
    # testReader('good.csv', ',', True, 17, 0)
    # testReader('bad.csv', ',', False, 18, 0)
    # testReader('bad.csv', ',', True, 17, 0)