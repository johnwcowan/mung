#!/usr/bin/env python

# The mung program

# Mung is an editor that, rather than fiddling with individual lines or
# characters, passes the entire file through a series of shell filters.
# The results of each filer are saved in a history along with metadata
# that allows reconstruction of how the munging was done.  The histories
# are kept in a history repository, by default $MUNG_ALL_REPOSITORIES.

# The commands allow the creation of a tree rather than just a sequence of
# states, and it's possible to display and move around the tree of states,
# creating new states at any point.  A state can be written back to the
# original file or to any other file.  An ordinary interactive editor can
# be run on a state to create a new state, and it's also possible for a
# new state to be created by reading in an existing file.

# States can be given a unique tag and a textual description, and its
# possible to display the whole tree or the metadata of a single state,
# and to page through the file associated with a particular state.

# Finally, a shell script that transforms the initial state into the
# current state can be written out.  This script can be run outside mung
# to transform any file into any other file.

import os
import sys
import shutil
import json

import g
import util
import repl

# Load the current state from the history directory
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
    g.stack = whole['stack']
    with open(os.path.join(g.history_dir, 'current'), 'r') as file:
       g.current = int(file.readline().rstrip())


def main():
    if len(sys.argv) != 2:
        print('usage: mung file', file=sys.stderr)
        sys.exit(1)
    g.pathname = sys.argv[1]
    if not os.path.exists(g.pathname):
        print(f'mung: {g.pathname} not found', file=sys.stderr)
        sys.exit(1)
    g.pathname = os.path.abspath(g.pathname)

    if not os.path.exists(g.history_repo):
        os.mkdir(g.history_repo)
        print(f'Created history repository at {g.history_repo}')
    result = os.stat(g.pathname)
    devino = str(result.st_dev) + '_' + str(result.st_ino)
    g.history_dir = os.path.join(g.history_repo, devino)
    if not os.path.exists(g.history_dir):
        os.mkdir(g.history_dir)
        util.newstate()
        print(f'Created history for {g.pathname}')
        print(f'  at {g.history_dir}')
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
