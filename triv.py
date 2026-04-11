# Trivially implemented commands

import sys

import g
import repl
import mung

def detag(tag):
    try:
        n = int(tag)
        if n < 0 or n > len(g.states):
            return None
        else:
           return n
    except ValueError:
        if tag in g.tags:
            return g.tags[tag]
        else:
            return None

def back(_):
    try:
        g.current = g.stack.pop()
        print(f'Now in state #{g.current}')
        mung.checkpoint()
    except IndexError:
        print('Nowhere to go back to')

def describe(desc):
    if desc is None:
        cmd = g.states[g.current]['cmd']
        desc = g.states[g.current]['desc']
        if desc == '':
            desc = "| " + cmd
        print(desc, end='')
    else:
        desc = repl.multiline(desc, False)
        g.states[g.current]['desc'] = desc + '\n'
        mung.checkpoint()

def destroy(_):
    if g.last_was_write:
        try:
            shutil.rmtree(g.history_dir)
        except PermissionError:
            print(f'State for {pathname} cannot be removed', file=sys.stderr)
        except FileNotFoundError:
            print(f'{pathname} is not being munged', file=sys.stderr)
        print('mung: terminating with history destroyed')
        exit(0)
    else:
       print('Write file and then destroy again')

def jump(newstate):
    if newstate is None:
        print('Unknown state or tag')
        return
    newstate = detag(newstate)
    g.stack.append(g.current)
    g.current = newstate
    print(f'Now in state #{g.current}')
    mung.checkpoint()

def quit(_):
    print('mung: terminating with history preserved')
    sys.exit(0)

def tag(newtag):
    if newtag is None:
        print('Must specify a tag')
        return
    try:
        _ = int(newtag)
    except ValueError:
        g.tags[newtag] = g.current
        mung.checkpoint()
        return
    print('Tag cannot be numeric')

def undo(_):
    try:
        newstate = g.states[g.current]['deps'][0]
    except IndexError:
        print('Nothing to undo')
        return
    g.stack.append(g.current)
    g.current = newstate
    print(f'Now in state #{g.current}')
    mung.checkpoint()

