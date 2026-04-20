# This file contains the global variables of mung,
# which represent the application state.  Threading
# them through all the calls would be unreasonably verbose,
# so all the modules import g to get access to them.

import os

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
