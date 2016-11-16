#!/usr/bin/env python

import os
import errno
from os.path import isfile, join

def image_dir(path):
  out = {'images': []}
  try:
    for img in os.listdir(path):
      if isfile(join(path, img)):
        schema = {
          'name': os.path.basename(img),
          'path': '/img/' + os.path.basename(img),
          'favorite': 'false',
        } 
        out['images'].append(schema)
  except OSError as e:
    if e.errno != errno.ENOTDIR:
      raise
  return out

if __name__ == '__main__':
  import json
  import sys

  try:
    dir_ = sys.argv[1]
  except IndexError:
    dir_ = "."

  print(json.dumps(image_dir(dir_), indent=2, sort_keys=True))
