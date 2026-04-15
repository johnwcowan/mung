# The mung command loop

import help
import script
import shell
import show
import triv

def repl():
    while True:
        try:
            cmd = input('* ')
            cmd = cmd.strip()
        except EOFError:
            print()
            triv.quit("")
        if cmd == '':
            continue
        if cmd[0] == '|':
            shell.pipe(cmd[1:])
            continue
        elif cmd[0] == '!':
            cmd = cmd[1:]
            shell.bang(cmd[1:])
            continue
        elif ' ' not in cmd:
           arg = None
        else:
            cmdarg = cmd.split(' ', 1)
            cmd = cmdarg[0]
            arg = cmdarg[1].strip()

        if cmd == 'describe' or cmd == 'd':
            triv.describe(arg)
        elif cmd == 'edit' or cmd == 'e':
            shell.edit(arg)
        elif cmd  == 'all' or cmd == 'a':
            show.all(arg)
        elif cmd == 'undo' or cmd == 'u':
            triv.undo(arg)
        elif cmd == 'edit' or cmd == 'e':
            shell.edit(arg)
        elif cmd  == 'all' or cmd == 'a':
            show.all(arg)
        elif cmd == 'undo' or cmd == 'u':
            triv.undo(arg)
        elif cmd == 'tag' or cmd == 't':
            triv.tag(arg)
        elif cmd == 'jump' or cmd == 'j':
            triv.jump(arg)
        elif cmd == 'back' or cmd == 'b':
            triv.back(arg)
        elif cmd == 'destroy':
            triv.destroy(arg)
        elif cmd == 'quit' or cmd == 'q':
            triv.quit(arg)
        elif cmd == 'read' or cmd == 'r':
            shell.read(arg)
        elif cmd == 'write' or cmd == 'w':
            shell.write(arg)
        elif cmd == 'mung' or cmd == 'm':
            script.mung(arg)
        elif cmd == 'show' or cmd == 's':
            show.show(arg)
        elif cmd == 'page' or cmd == 'p':
            shell.page(arg)
        elif cmd == 'help' or cmd == 'h':
            help.help(arg)
        else:
            print(f'No command "{cmd}"')

