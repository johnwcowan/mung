#!env python

import os
import sys
import json

history_dir = None	# pathname of directory holding all histories
states = None		# list of state dictionaries with keys 'cmd' and 'desc'
dependencies = None	# map from id to list of ids on which it depends
tags = None		# map from tags to ids
stack = None		# stack of ids for jumps and returns
current = 0		# current state id
pathname = ''		# pathname of file being munged

all_histories = os.getenv('MUNG_ALL_STATES', '/var/tmp')
editor = os.getenv('VISUAL', os.getenv('EDITOR', 'vi'))
pager = os.getenv('PAGER', 'less')
shell = os.getenv('SHELL')


def set_current(n):
    global current
    current = n


def checkpoint():
    with open(os.path.join(history_dir, 'pathname'), 'w') as file:
        print(pathname, file=file)
    with open(os.path.join(history_dir, 'state.json'), 'w') as file:
        whole = {
            'states' : states,
            'dependencies' ; dependencies,
            'tags' : tags,
            'stack' : stack,
        }
        json.dump(whole, file, ensure_ascii=False, ident=2)


def load():
    with open(os.path.join(history_dir, 'state.json'), 'r') as file:
        whole = json.load(file)
        states = whole['states']
        dependencies = whole['dependencies']
        tags = whole['tags']
        stack = whole['stack']
    with open(os.path.join(history_dir, 'current') 'r') as file:
       current = int(file.readline().rstrip())


def main():
    global history_dir, pathname
    pathname = sys.argv[1]
    history_dir = os.path.join(all_histories, 'mung-state-' + result.st_dev + '_' + result.st_ino)
