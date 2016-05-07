"""Utility functions for quickly reading and writing files.

.. moduleauthor:: Seth-David Donald Dworman <sdworman@brandeis.edu>

"""

import json
import os

import bs4

def remove_unicode(string):
    return ''.join([x for x in string if ord(x) < 128])

def read_file(input_file):
    with open(input_file, 'r') as f:
        return f.read()

def write_file(output_file, content):
    with open(output_file, 'w') as f:
        f.write(content)
    return output_file

def read_list(input_file):
    l = []
    with open(input_file, 'r') as f:
        for line in f:
            l.append(line.strip('\n'))
    return l

def write_json(output_file, obj, indent=2):
    pretty = json.dumps(obj, indent=indent)
    write_file(output_file, pretty)
    
def get_soup(input_file, parser='html.parser'):
    return bs4.BeautifulSoup(read_file(input_file), parser)


if __name__ == '__main__':
    pass
