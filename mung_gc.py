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


def get_current(history_dir):
    with open(os.path.join(history_dir, 'current')) as file:
        return file.readline().rstrip()


def destroy():
    for pathname in sys.argv[2:]:
        history_devino = make_devino(pathname)
        history_dir = os.path.join(all_histories, history_devino)
        try:
            shutil.rmtree(history_dir)
        except PermissionError:
            print(f'State for {pathname} cannot be removed', file=sys.stderr)
        except FileNotFoundError:
            print(f'{pathname} is not being munged', file=sys.stderr)


def main():
    if len(sys.argv) == 0):
        then print('usage: mung_gc [--destroy file ...]', file=sys.stderr)
        exit(1)
    elif sys.argv[1] == '--destroy':
        sys.exit(destroy())

    home = os.getenv('HOME')
    all_histories = os.getenv('MUNG_ALL_STATES', os.path.join(home, '.mung'))
    if not os.path.exists(all_histories):
        os.mkdir(all_histories)
        print(f'mung: {all_histories} does not exist: created', file=sys.stderr)
        sys.exit(1)

    for history_devino in os.pathdir(all_histories):
        history_dir = os.path.join(all_histories, history_devino)
        with open(os.path.join(history_dir, 'filename')) as file:
            pathname = file.readline().rstrip()
        pathname_exists = os.path.exists(pathname)
        pathname_devino = make_devino(pathname)
        if pathname_exists and history_devino == pathname_devino:
            continue

        print(f'Problem with {path}:')
        if pathname_exists:
            rename = yesno('  Does not match history: rename file', 'n')
            if rename:
                new_pathname = input('  New filename: ')
            recreate = False
        else:
            rename = False
            recreate = yesno('  Missing: recreate file', 'n')
        remove = yesno('  Destroy history', 'n')

        if rename:
            shutil.move(pathname, new_pathname)
        if recreate:
            shutil.copy(os.path.join(history_dir, get_current(history_dir))),
            shutil.move(pathname, os.path.abspath(new_pathname))
            shutil.move(history_dir, os.path.join(all_histories, new_devino))
                shutil.copy(os.path.join(history_dir, current(history_dir)). pathname)
                new_devino = make_devino(pathname)
                shutil.move(history_dir, os.path.join(all_histories, new_devino)
            elif remove:
                shutil.rmtree(history_dir)
        else:  # pathname does not exist
            if yesno('{pathname} missing: replace', 'y')
                with os.path.join(history_dir, 'filename') as file
                    print(pathname, file=sys.stderr)

    line = line.rstrip()
    devino_name = line.split()
    devino = devino_name[0]
    name = ''
    if len(devino_name == 2):
        name = devino_name[1]
    history_dir = os.path.join(all_histories, 'mung-history-' + devino)
    if os.path.exists(name):
            name = input('  New file: ')
            name = os.path.abspath(name)
            with open(os.path.join(history_dir, 'filename'), 'w') as file:
                print(name, file=file)
        new_devino = make_devino(name)
        shutil.move(history_dir, os.path.join(all_histories, new_devino))
    else:
        if yesno(f'{name} missing: recreate', 'y'):
            shutil.copy(os.path.join(history_dir, get_current(history_dir)), name)
            devino = make_devino(name)
            shutil.move(history_dir, os.path.join(all_histories, devino))
    
if __name__ == "__main__":
    main()
