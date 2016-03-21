#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
# +++your code here+++
def find_special(dir):
  paths = []
  filenames = os.listdir(dir)
  for filename in filenames:
    if re.search(r'__\w+__', filename):
      path = os.path.join(dir, filename)
      paths.append(os.path.abspath(path))
  return paths

# --todir: takes in paths and to_dir in which we will put the 
# files that the paths direct to
def place_special(paths, to_dir):
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for path in paths:
    filename = os.path.basename(path)
    shutil.copy(path, os.path.join(to_dir, filename))

# --tozip 
# usage: 'zip -j yourzip.zip pwd pwd'
def zip_to(paths, zipfile):
  cmd = 'zip -j ' + zipfile + ' '.join(paths)
  (status, output) = commands.getstatusoutput(cmd)

  if status:
    sys.stderr.write(output)
    sys.exit(1)
# Write functions and modify main() to call them

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = []
  for dirname in args:
    paths.extend(find_special(dirname))

  if todir:
    place_special(paths, todir)
  elif tozip:
    zip_to(paths, tozip)
  else:
    print '\n'.join(paths)
  
if __name__ == "__main__":
  main()
