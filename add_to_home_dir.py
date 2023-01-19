#!/usr/bin/env python3

import os

import sys
from pathlib import Path
import re
y = re.compile("href\s*=\s*\"..")
ysrc = re.compile("src\s*=\s*\"..")

def main():
    os.chdir('html')
    files = os.listdir('.')
    for x in files:
        file_read = open(x, 'r+')
        file_wt = open(os.path.join('..', x), 'w+')
        line = file_read.read()
        fx = y.sub('href=\"', line)
        fx = ysrc.sub('src=\"', fx)
        file_wt.write(fx)
        file_wt.close()
        file_read.close()


if __name__ == "__main__":
    main()