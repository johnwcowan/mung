#!/usr/bin/env python

import os
import sys
import shutil
import json

import script
import shell
import show
import triv

pathname = ''		# pathname of file being munged
history_dir = None	# pathname of directory holding all histories
states = None		# list of state dictionaries with keys 'cmd' and 'desc'
dependencies = None	# map from id to list of ids on which it depends
tags = None		# map from tags to ids
stack = None		# stack of ids for jumps and returns
current = 0		# current state id

home = os.getenv('HOME')

editor = os.getenv('VISUAL', os.getenv('EDITOR', 'vi'))
pager = os.getenv('PAGER', 'less')
shell = os.getenv('SHELL')
all_histories = os.getenv('MUNG_HISTORIES',
                          os.path.join(home, '.mung'))


def set_current(n):
    global current
    current = n
    checkpoint()


def checkpoint():
    with open(os.path.join(history_dir, 'pathname'), 'w') as file:
        print(pathname, file=file)
    with open(os.path.join(history_dir, 'state.json'), 'w') as file:
        whole = {
            'states' : states,
            'dependencies' : dependencies,
            'tags' : tags,
            'stack' : stack,
        }
        json.dump(whole, file, ensure_ascii=False, ident=2)
    with open(os.path.join(history_dir, 'current')) as file:
        print(current, file=file)


def load():
    with open(os.path.join(history_dir, 'pathname'), 'r') as file:
        saved_pathname = file.readline().rstrip()
    if saved_pathname != pathname:
        print(f'mung: {pathname} does not match state: run mung_gc', file=sys.stderr)
        sys.exit(1)
    with open(os.path.join(history_dir, 'state.json'), 'r') as file:
        whole = json.load(file)
    states = whole['states']
    dependencies = whole['dependencies']
    tags = whole['tags']
    stack = whole['stack']
    with open(os.path.join(history_dir, 'current'), 'r') as file:
       current = int(file.readline().rstrip())


def init():
    global states, dependencies, tags, stack
    states = [{"cmd" : "", "desc" : ""}]
    dependencies = {0 : []}
    tags = {}
    stack = []
    checkpoint()


def main():
    global history_dir, pathname
    if len(sys.argv) != 2:
        print('usage: mung file')
        sys.exit(1)
    pathname = sys.argv[1]
    if not os.path.exists(pathname):
        print(f'mung: {pathname} not found', file=sys.stderr)
        sys.exit(1)
    pathname = os.path.abspath(pathname)
    result = stat(pathname)
    history_dir = os.path.join(all_histories, result.st_dev + '_' + result.st_ino)
    if not exists(history_dir):
        init()
        print('Created history at {history_dir} for {pathname}')
    else:
        load(history_dir)
        print('Loaded {len(states) states')
    repl.repl()

    
if __name__ == "__main__":
    main()
