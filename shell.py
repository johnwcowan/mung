# Commands that interact with the file system

import os
import shutil

import g
import util

# create new state
def newstate():
    pass

def pipe(cmd):
    pass

def edit(_):
    pass

def page(_):
    pathname = os.path.join(g.history_dir, str(g.current))
    os.system(f'{g.pager} {g.pathname}')

def read(filename):
    pass

def write(filename):
    pass

def bang(cmd):
    pass
