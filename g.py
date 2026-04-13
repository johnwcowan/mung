# This file contains the global variables of mung,
# which represent the application state.  Threading
# them through all the calls would be unreasonably verbose,
# so all the modules import g to get access to them.

import os

home = os.getenv('HOME')
history_repo = os.getenv('MUNG_REPOSITORY',
                         os.path.join(home, '.local/share/mung'))
history_dir = None	# pathname of directory holding history

pathname = ''		# pathname of file being munged
states = None		# list of state dictionaries with keys 'cmd' and 'desc'
tags = None		# map from tags to ids
jump_stack = None	# stack of ids for jumps and returns
undo_stack = None	# stack of ids for jumps and returns
current = 0		# current state id
last_was_write = False	# last command was a write

editor = os.getenv('VISUAL', os.getenv('EDITOR', 'vi'))
pager = os.getenv('PAGER', 'less')
shell = os.getenv('SHELL')
