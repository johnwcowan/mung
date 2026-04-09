#!/usr/bin/env python

import os
import sys
import shutil
import json

import g
import repl


def checkpoint():
    whole = {
        'states' : g.states,
        'tags' : g.tags,
        'jump_stack' : g.jump_stack,
        'undo_stack' : g.undo_stack,
    }
    with open(os.path.join(g.history_dir, 'pathname'), 'w') as file:
        print(g.pathname, file=file)
    with open(os.path.join(g.history_dir, 'state.json'), 'w') as file:
        json.dump(whole, file, ensure_ascii=False, indent=2)
        print(file=file)
    with open(os.path.join(g.history_dir, 'current'), 'w') as file:
        print(g.current, file=file)


def load():
    with open(os.path.join(g.history_dir, 'pathname'), 'r') as file:
        saved_pathname = file.readline().rstrip()
    if saved_pathname != g.pathname:
        print(f'mung: {g.pathname} does not match state: run mung_gc',
              file=sys.stderr)
        sys.exit(1)
    with open(os.path.join(g.history_dir, 'state.json'), 'r') as file:
        whole = json.load(file)
    g.states = whole['states']
    g.tags = whole['tags']
    g.jump_stack = whole['jump_stack']
    g.undo_stack = whole['undo_stack']
    with open(os.path.join(g.history_dir, 'current'), 'r') as file:
       g.current = int(file.readline().rstrip())


def init():
    os.mkdir(g.history_dir)
    g.states = [{
        'cmd' : '',
        'desc' : '',
        'parent' : None,
        'deps' : []
    }]
    g.tags = {}
    g.jump_stack = []
    g.undo_stack = []
    shutil.copy(g.pathname, os.path.join(g.history_dir, '0'))
    checkpoint()


def main():
    if len(sys.argv) != 2:
        print('usage: mung file')
        sys.exit(1)
    g.pathname = sys.argv[1]
    if not os.path.exists(g.pathname):
        print(f'mung: {g.pathname} not found', file=sys.stderr)
        sys.exit(1)
    g.pathname = os.path.abspath(g.pathname)

    if not os.path.exists(g.history_repo):
        os.mkdir(g.history_repo)
        print(f'Created g.history repository at {g.history_repo}')
    result = os.stat(g.pathname)
    devino = str(result.st_dev) + '_' + str(result.st_ino)
    g.history_dir = os.path.join(g.history_repo, devino)
    if not os.path.exists(g.history_dir):
        init()
        print(f'Created history at {g.history_dir} for {g.pathname}')
    else:
        load()
        count = len(g.states)
        if count == 1:
            print(f'Loaded 1 state: current state is #0')
        else:
            print(f'Loaded {count} states: current state is #{g.current}')
    repl.repl()

    
if __name__ == "__main__":
    main()
