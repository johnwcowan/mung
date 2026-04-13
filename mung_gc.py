#!/usr/bin/env python3

# The mung-gc command runs a garbage collector over the master history
# directory and makes the files in the tree agree with the histories.
# This happens when the file being munged is deleted or replaced but the
# history is not removed.

# Here's what is done.  Read through the directory of all histories,
# which is $MUNG_ALL_HISTORIES (or by default $HOME/.mung)   The file
# whose pathname appears in "pathname" in each history directory is
# checked to determine its device and inode numbers, which are an absolute
# identification of the file (they do not change if the file is renamed
# or rewritten).  If the file exists and its device and inode numbers
# match the name of the history directory, all is well, and we move on to
# the next history.

# Otherwise, if the file exists, ask about moving it somewhere else (prompt
# for the new name).  If it does not exist, ask about restoring it from
# the current state. In either case, ask about destroying the history.

# This file is self-contained and is not part of the mung command.

import os
import shutil
import sys


def make_devino(name):
    result = os.stat(name)
    return '_'.join(str(result.st_dev), str(result.st_ino))


# Ask a yes or no question (the prompt has already been printed)
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


# Extract the current state from the "current" file in a history directory
def get_current(history_dir):
    with open(os.path.join(history_dir, 'current')) as file:
        return file.readline().rstrip()


# Destroy the histories given on the command line directory
def destroy():
    for pathname in sys.argv[2:]:
        history_devino = make_devino(pathname)
        history_dir = os.path.join(history_repo, history_devino)
        try:
            shutil.rmtree(history_dir)
        except PermissionError:
            print(f'State for {pathname} cannot be removed', file=sys.stderr)
        except FileNotFoundError:
            print(f'{pathname} is not being munged', file=sys.stderr)


# The main program
def main():
    if len(sys.argv) == 0:
        print('usage: mung_gc [--destroy file ...]', file=sys.stderr)
        exit(1)
    elif sys.argv[1] == '--destroy':
        sys.exit(destroy())

    # Set up the variables and create the history repository if needed
    home = os.getenv('HOME')
    history_repo = os.getenv('MUNG_REPOSITORY',
                             os.path.join(home, '.local/share/mung'))
    if not os.path.exists(history_repo):
        os.mkdir(history_repo)
        print(f'mung: {history_repo} does not exist', file=sys.stderr)
        sys.exit(1)

    # Walk through the history directories
    for history_devino in os.pathdir(history_repo):
        history_dir = os.path.join(history_repo, history_devino)
        with open(os.path.join(history_dir, 'filename')) as file:
            pathname = file.readline().rstrip()
        pathname_exists = os.path.exists(pathname)
        pathname_devino = make_devino(pathname)
        if pathname_exists and history_devino == pathname_devino:
            continue

        # Interact with the user for a problematic history directory
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

        # Copy, move, and rewrite files
        if rename:
            shutil.move(pathname, new_pathname)
        if recreate:
            shutil.copy(os.path.join(history_dir, get_current(history_dir))),
            shutil.move(pathname, os.path.abspath(new_pathname))
            shutil.move(history_dir, os.path.join(history_repo, new_devino))
            shutil.copy(os.path.join(history_dir, current(history_dir)). pathname)
                new_devino = make_devino(pathname)
                shutil.move(history_dir, os.path.join(history_repo, new_devino)
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
    history_dir = os.path.join(history_repo, devino)
    if os.path.exists(name):
            name = input('  New file: ')
            name = os.path.abspath(name)
            with open(os.path.join(history_dir, 'filename'), 'w') as file:
                print(name, file=file)
        new_devino = make_devino(name)
        shutil.move(history_dir, os.path.join(history_repo, new_devino))
    else:
        if yesno(f'{name} missing: recreate', 'y'):
            shutil.copy(os.path.join(history_dir, get_current(history_dir)), name)
            devino = make_devino(name)
            shutil.move(history_dir, os.path.join(history_repo, devino))
    
if __name__ == "__main__":
    main()
