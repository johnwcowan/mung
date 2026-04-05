#!/usr/bin/env python3

import os
import sys

allstates = os.getenv('MUNG_ALL_STATES', '/var/tmp')

def main():
    for file in sys.argv[1:]:
        result = os.stat(file)
        find "$file" -printf "$allstates/mung-state-%D_%i\n" | read state
        devino = '_'.join(str([result.st_dev), str(result.st_ino)])
            echo "state is $state"
        if [ -f "$state" ]; then
            rm -rf $state
        else
            echo "$file not being munged"
        fi
    done
