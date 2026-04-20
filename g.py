# This file contains the global variables of mung,
# which represent the application state.  Threading
# them through all the calls would be unreasonably verbose,
# so all the modules import g to get access to them.
# It also contains utility functions used in more than one module.

import os
import json

# The history repository pathname is $MUNG_REPOSITORY,
# or failing that it is $XDG_STATE_HOME/mung,
# or failing that it is $HOME/.local/share/mung.
home = os.getenv('HOME')
state_home = os.getenv('XDG_STATE_HOME')
history_repo = os.getenv('MUNG_REPOSITORY')
if history_repo is not None:
    pass
elif state_home is not None:
    history_repo = os.path.join(state_home, 'mung')
else:
    history_repo = os.path.join(home, '.local/state/mung')

history_dir = None	# pathname of directory holding history
pathname = ''		# pathname of file being munged
states = []		# list of state dictionaries with keys 'cmd' and 'desc'
tags = {}		# map from tags to ids
stack = []		# stack of ids for jumps and returns
current = 0		# current state id
last_was_write = False	# last command was a write

# External commands
editor = os.getenv('VISUAL', os.getenv('EDITOR', 'vi'))
pager = os.getenv('PAGER', 'less')
shell = os.getenv('SHELL')



# Save the current state tp the history directory
def save():
    whole = {
        'states' : states,
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


def multiline(line, keep):
    while True:
        if line[-1] != '\\':
            return line
        else:
            if not keep:
                line = line[0:-1]
            line += '\n' + input('> ')


# escape ' within shell single quotes
def escape(path):
    return "'" + path.replace("'", "'\\''") + "'" 


# create a new state
def newstate():
    newcurrent = len(states)
    state = {
        'cmd' : '',
        'mode' : None,
        'desc' : '',
        'parent' : None,
        'deps' : []
    }
    states.append(state)
    return newcurrent, state


