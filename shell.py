# Commands that interact with the file system

import os
import shutil
import sys

import g
import util


def pipe(cmd):
    cmd = util.multiline(cmd, True)
    newcurrent, state = util.newstate()
    state['cmd'] = cmd
    state['mode'] = 'pipe'
    state['parent'] = g.current
    new_pathname = os.path.join(g.history_dir, str(newcurrent))
    old_pathname = os.path.join(g.history_dir, str(g.current))
    os.system(f' <{old_pathname} cmd >{new_pathname}')
    g.current = newcurrent
    util.save()


def edit(_):
    newcurrent, state = util.newstate()
    state['cmd'] = None
    state['mode'] = 'edit'
    state['parent'] = g.current
    new_pathname = os.path.join(g.history_dir, str(newcurrent))
    old_pathname = os.path.join(g.history_dir, str(g.current))
    shutil.copy(old_pathname, new_pathname)
    os.system(f'{g.editor} {new_pathname}')
    g.current = newcurrent
    util.save()



def page(pager):
    if pager is None:
        pager = g.pager
    pathname = os.path.join(g.history_dir, str(g.current))
    os.system(f'{pager} {pathname}')


def read(filename):
    source_pathname = os.path.join(os.getcwd(), filename)
    newcurrent, state = util.newstate()
    state['cmd'] = source_pathname
    state['mode'] = 'file'
    state['parent'] = g.current
    state_pathname = os.path.join(g.history_dir, str(newcurrent))
    shutil.copy(source_pathname, state_pathname)
    g.current = newcurrent
    util.save()


# Write the current state file to filename
def write(filename):
    if filename is None:
        filename = g.pathname
    try:
        shutil.copy(os.path.join(g.history_dir, str(g.current)), filename)
    except PermissionError:
        print(f'mung: cannot write {filename}', file=sys.stderr)


# Execute a shell command.  No effect on mung's data structures.
def bang(cmd):
    cmd = util.multiline(cmd, True)
    os.system(cmd)
