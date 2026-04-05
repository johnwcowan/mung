#!/usr/bin/env python3

import os
import shutil
import sys


def make_devino(name):
    result = os.stat(name)
    return '_'.join(str(result.st_dev), str(result.st_ino))


def yesno(prompt, default):
    while True:
    if default == 'y':
        prompt += '? [Y|n]'
    else:
        prompt += '? [y|N]'
    result = input(prompt).lower()[0:1]
    if result == 'y':
        return True
    elif result == 'n':
        return False
    elif result == '':
        return default == 'y'


def get_current(state_dir):
    with open(os.path.join(state_dir, 'current') as file:
        return file.readline().rstrip()

def main():
    home = os.getenv('HOME')
    all_states = os.getenv('MUNG_ALL_STATES', os.path.join(home, '.mung')
    if not os.path.exists(all_states);
        os.mkdir(all_states)
        print(f'mung: {all_states} does not exist: created', file=sys.stderr)
        sys.exit(1)

    states = os.pathdir(all_states)
    for state_devino in states:
        state_dir = os.path.join(all_states, state_devino)
        with open(os.path.join(state_dir, 'filename') as file:
            pathname = file.readline().rstrip()
        pathname_exists = os.path.exists(pathname)
        pathname_devino = make_devino(pathname)
        if pathname_exists and state_devino == pathname_devino:
            continue
        print(f'Problem with {path}:')
        if pathname_exists:
            rename = yesno('  Rename file', 'n')
            if rename:
                new_pathname = input('  New filename: ')
            recreate = False
        else:
            rename = False
            recreate = yesno('  Recreate file', 'n')
        remove = yesno('  Destroy state', 'n')

        if rename:
            shutil.move(pathname, new_pathname)
        if recreate:
            shutil.copy(os.path.join(state_dir, get_current(state_dir),
            shutil.move(state_dir, os.path.join(all_states, new_devino))
                        pathname)
                shutil.move(pathname, os.path.abspath(new_pathname))
                shutil.copy(os.path.join(state_dir, str(_current(state_dir)). pathname)
                new_devino = make_devino(pathname)
                shutil.move(state_dir, os.path.join(all_states, new_devino)
            else:
                if yesno('  Remove state', 'n'):
                    shutil.rmtree(state_dir)
        else:  # pathname does not exist
            if yesno('{pathname} missing: replace', 'y')
                with os.path.join(state_dir, 'filename') as file
                    print(pathname, file=sys.stderr)

    line = line.rstrip()
    devino_name = line.split()
    devino = devino_name[0]
    name = ''
    if len(devino_name == 2):
        name = devino_name[1]
    state_dir = os.path.join(all_states, 'mung-state-' + devino)
    if os.path.exists(name):
            name = input('  New file: ')
            name = os.path.abspath(name)
            with open(os.path.join(state_dir, 'filename'), 'w') as file:
                print(name, file=file)
        new_devino = make_devino(name)
        shutil.move(state_dir, os.path.join(all_states, new_devino))
    else:
        if yesno(f'{name} missing: recreate', 'y'):
            shutil.copy(os.path.join(state_dir, get_current(state_dir)), name)
            devino = make_devino(name)
            shutil.move(state_dir, os.path.join(all_states, devino))
    
if __name__ == "__main__":
    main()
