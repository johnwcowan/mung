# Trivially implemented commands

import sys
import shutil

import g
import repl

def detag(tag):
    try:
        n = int(tag)
        if n < 0 or n > len(g.states) - 1:
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
        print(f'Now in state #{g.current}', file=sys.stderr)
        g.save()
    except IndexError:
        print('Nowhere to go back to', file=sys.stderr)

def describe(desc):
    if desc is None or desc == '':
        cmd = g.states[g.current]['cmd']
        desc = g.states[g.current]['desc']
        if desc == '' and cmd != '':
            desc = "| " + cmd
        elif desc == '':
            print('(none)')
        print(desc)
    else:
        desc = g.multiline(desc, False)
        g.states[g.current]['desc'] = desc
        g.save()

def destroy(_):
    if g.last_was_write:
        try:
            shutil.rmtree(g.history_dir)
        except PermissionError:
            print(f'State for {pathname} cannot be removed', file=sys.stderr)
        except FileNotFoundError:
            print(f'{pathname} is not being munged', file=sys.stderr)
        print('mung: terminating with history destroyed', file=sys.stderr)
        exit(0)
    else:
       print('Write file and then destroy again', file=sys.stderr)

def jump(newstate):
    newstate = detag(newstate)
    if newstate is None:
        print('Unknown state or tag', file=sys.stderr)
    g.stack.append(g.current)
    g.current = newstate
    g.save()

def quit(_):
    print('mung: terminating with history preserved', file=sys.stderr)
    sys.exit(0)

def tag(newtag):
    if newtag is None:
        print('Must specify a tag', file=sys.stderr)
        return
    try:
        _ = int(newtag)
    except ValueError:
        g.tags[newtag] = g.current
        g.save()
        return
    print('Tag cannot be numeric', file=sys.stderr)

def undo(_):
    newcurrent = g.states[g.current]['parent']
    if newcurrent is None:
        print('Nothing to undo', file=sys.stderr)
        return
    g.stack.append(g.current)
    g.current = newcurrent
    print(f'Now in state #{g.current}', file=sys.stderr)
    g.save()

