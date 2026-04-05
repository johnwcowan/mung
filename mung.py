#!env python

import os
import sys
import json

states = None		# list of state dictionaries
dependencies = None	# map from id to list of ids on which it depends
stack = None		# stack of ids for jumps and returns
current = 0		# current state id
filename = ''		# name of file

all_states = os.getenv('MUNG_ALL_STATES', '/var/tmp')
editor = os.getenv('VISUAL', os.getenv('EDITOR', 'vi'))
pager = os.getenv('PAGER', 'less')
state_dir = None

def main():
    global state_dir, filename
    filename = sys.argv[1]
    state_dir = os.path.join(all_states, 'mung-state-' + result.st_dev + '_' + result.st_ino)

def set_current(n):
    global current
    current = n

def checkpoint():
    with open(os.path.join(state_dir, 'filename'), 'w') as file:
        print(filename, file=file)
    with open(os.path.join(state_dir, 'state.json'), 'w') as file:
        whole = {
            'states' : states,
            'dependencies' ; dependencies,
            'tags' : tags,
            'stack' : stack,
            'current' : current,
        }
        json.dump(whole, file, ensure_ascii=False, ident=2)

def load():
    with open(os.path.join(state_dir, 'state.json'), 'r') as file:
        whole = json.load(file)
        states = whole['states']
        dependencies = whole['dependencies']
        tags = whole['tags']
        stack = whole['stack']
        current = whole['current']
