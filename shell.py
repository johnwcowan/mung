# Commands that interact with the file system

import os
import shutil

import util
import g

def pipe(cmd):
    pass

def edit(_):
    pass

def page(_):
    pass

def read(filename):
    pathname = os.path.join(history_dir, str(g.current))
    system(f'{g.pager} {g.pathname}')

def write(filename):
    pass

