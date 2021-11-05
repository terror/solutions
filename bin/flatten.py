#!/usr/bin/python3

import shutil
import os

def move(dest):
  a, f = [], 1
  for root, _, files in os.walk(dest):
    if f:
      f ^= 1
      continue
    for name in files:
      a.append(os.path.join(root, name))
  for name in a:
    shutil.move(name, dest)

if __name__ == '__main__':
  move(input("path: "))
