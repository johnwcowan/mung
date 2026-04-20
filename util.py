# Utility functions

import os
import json

import g

# Save the current state tp the history directory
def save():
    whole = {
        'states' : g.states,
        'tags' : g.tags,
        'stack' : g.stack,
    }
    with open(os.path.join(g.history_dir, 'pathname'), 'w') as file:
        print(g.pathname, file=file)
    with open(os.path.join(g.history_dir, 'state.json'), 'w') as file:
        json.dump(whole, file, ensure_ascii=False, indent=2)
        print(file=file)
    with open(os.path.join(g.history_dir, 'current'), 'w') as file:
        print(g.current, file=file)


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
    newcurrent = len(g.states)
    state = {
        'cmd' : '',
        'mode' : None,
        'desc' : '',
        'parent' : None,
        'deps' : []
    }
    g.states.append(state)
    return newcurrent, state


# Given a state number, return a tag
def get_tag(n):
    for tag in g.tags:
        if g.tags[tag] == n:
            return tag
    return None

