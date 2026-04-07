#!/usr/bin/env python

import os
import sys
import shutil
import json

import repl

home = os.getenv('HOME')
history_repo = os.getenv('MUNG_REPOSITORY', os.path.join(home, '.mung'))
history_dir = None	# pathname of directory holding history

pathname = ''		# pathname of file being munged
states = None		# list of state dictionaries with keys 'cmd' and 'desc'
dependencies = None	# map from id to list of ids on which it depends
tags = None		# map from tags to ids
stack = None		# stack of ids for jumps and returns
current = 0		# current state id
last_was_write = False	# last command was a write


editor = os.getenv('VISUAL', os.getenv('EDITOR', 'vi'))
pager = os.getenv('PAGER', 'less')
shell = os.getenv('SHELL')


def set_current(n):
    global current
    current = n
    checkpoint()


def checkpoint():
    whole = {
        'states' : states,
        'dependencies' : dependencies,
        'tags' : tags,
        'stack' : stack,
    }
    with open(os.path.join(history_dir, 'pathname'), 'w') as file:
        print(pathname, file=file)
    with open(os.path.join(history_dir, 'state.json'), 'w') as file:
        json.dump(whole, file, ensure_ascii=False, indent=2)
        print(file=file)
    with open(os.path.join(history_dir, 'current'), 'w') as file:
        print(current, file=file)


def load():
    global states, dependencies, tags, stack, current
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
    os.mkdir(history_dir)
    global states, dependencies, tags, stack
    states = [{"cmd" : "", "desc" : ""}]
    dependencies = {0 : []}
    tags = {}
    stack = []
    shutil.copy(pathname, os.path.join(history_dir, '0'))
    checkpoint()
    print(f'Created history at {history_dir} for {pathname}')


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

    if not os.path.exists(history_repo):
        os.mkdir(history_repo)
        print(f'Created history repository at {history_repo}')
    result = os.stat(pathname)
    devino = str(result.st_dev) + "_" + str(result.st_ino)
    history_dir = os.path.join(history_repo, devino)
    if not os.path.exists(history_dir):
        init()
    else:
        load()
        print(f'Loaded {len(states)} state(s): current state is #{current}')
    repl.repl()

    
if __name__ == "__main__":
    main()
