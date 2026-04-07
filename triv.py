import sys

import mung

def detag(arg):
    try:
        n = int(arg)
        return int(n)
    except ValueError:
        if arg in mung.tags:
            return mung.tags[arg]
        else:
            return None

def back(arg):
    pass

def describe(arg):
    if arg is None:
        try:
            cmd = mung.states[mung.current]['cmd']
            desc = mung.states[mung.current]['desc']
            if desc == '':
                desc = "|" + cmd
            print(f'State #{mung.current} is "{desc}"')
        except KeyError:
            print('No description')
    else:
        mung.states[mung.current]['desc'] = arg
        mung.checkpoint()

def destroy(arg):
    if mung.last_was_write:
      shutil.rmtree(mung.history_dir)
      print('State destroyed')
      exit(0)
    else:
       print('Write file and repeat destroy')

def jump(arg):
    pass

def quit(arg):
    print('mung: terminating with states preserved')
    sys.exit(0)

def tag(arg):
    pass

def undo(arg):
    pass

def unundo(arg):
    pass

