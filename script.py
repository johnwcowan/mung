# Create a shell script

import sys

import g

# Collect all relevant states into the workspace
def collect(workspace, id):
    if id in workspace:
        return
    # Do nothing if this state has been collected
    state = g.states(id)
    workspace[id] = copy.deepcopy(state)
    # Recursively collect the parent state
    collect(workspace, state['parent'])
    # Recursively collect the states depended on
    for depid in deps:
        collect(workspace, depid)

# Merge pipelines
def merge(workspace):
    pass

# Topologically sort remaining states
def tsort(workspace):
    pass

# Generate a script from initial state to current state
def mung(filename):
    if (filename is None):
        print('Script file name not specified')
    workspace = {}
    collect(workspace, g.current)
    merge(workspace)
    result = tsort(workspace)
    with open(filename, 'w') as file:
        print(result, end='')
        return
