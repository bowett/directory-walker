#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import csv
import argparse

def has_hidden_dirs(list_of_dirs):
    for each_dir in list_of_dirs:
        if each_dir is not '':
            if each_dir[0] == '.':
                return True
    return False

parser = argparse.ArgumentParser()
parser.add_argument("--path", help="The path of the directory to walk over")
parser.add_argument("--output", help="The path of the output file the script produces")
parser.add_argument("--withhidden", action="store_true", help="If included the output will include hidden files and directories")
args = parser.parse_args()


target_dir = os.getcwd()
if args.path is not None:
    # Test to see if the given path is a valid directory
    if os.path.isdir(args.path):
        target_dir = args.path
    else:
        sys.exit("Error: " + args.path + " is not a valid path")

output = './output.csv'
if args.output is not None:
    output = args.output

    # Check if we have write permissions to the output file
    if os.access(os.path.dirname(output), os.W_OK):
        #the file does not exists but write privileges are given
        print 'Have permission'
    else:
        print 'No permission'

print 'Starting to walk ' + target_dir

data = []
for root, dirs, files in os.walk(target_dir):
    if args.withhidden:
        for f in files:
            l = root.split(os.path.sep) + [f]
            data.append(l)
    else:
        for f in files:
            l = root.split(os.path.sep) + [f]
            if not has_hidden_dirs(l):
                if not f[0] == '.':
                    data.append(l)

print 'Outputting data to ' + output

with open(output, 'wb') as f:
    writer = csv.writer(f)
    for d in data:
        if ".DS_Store" not in d:
            writer.writerow(d)
