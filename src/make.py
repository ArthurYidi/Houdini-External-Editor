#!/usr/bin/env python

import os
from glob import glob

VERSION = '0.0.2'

def main():
    with open('script.py', 'r') as f:
        script = f.read()

    for template in glob('*.template'):
        with open(template, 'r') as t_f:
            parsed = t_f.read()
            parsed = parsed.format(version=VERSION, script=script)
            output, _ = os.path.splitext(template)
            output = '../' + output
            with open(output, 'w') as o_f:
                o_f.write(parsed)

if __name__ == '__main__':
    main()
