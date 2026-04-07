def repl():
    while True:
        try:
            cmd = input(':')
        except EOFError:
            triv.quit()
        if cmd[0] = '|':
            shell.pipe(cmd[1:])
            continue
        elif cmd[0] == '!'
            cmd = cmd[1:]
            shell.bang(cmd[1:])
            continue
        elif ' ' not in args:
           args = None
        else:
            cmd, args = cmd.split(' ', 1)
            args = args.strip()

    elif arg == 'describe' or arg == 'd':
        triv.describe():
    elif arg == 'edit' or arg == 'e':
        shell.edit():
    elif arg  == 'all' or arg == 'a':
        show.all():
    elif arg == 'undo' or arg == 'u':
        triv.undo():
    elif arg == 'unundo' or arg == 'uu':
        triv.unundo():
    elif arg == 'choices' or arg == 'c':
        show.choices():
    elif arg == 'tag' or arg == 't':
        triv.tag():
    elif arg == 'jump' or arg == 'j':
        triv.jump():
    elif arg == 'back' or arg == 'b':
        triv.back():
    elif arg == 'destroy':
        triv.destroy():
    elif arg == 'quit' or arg == 'q':
        triv.quit():
    elif arg == 'read' or arg == 'r':
        shell.read():
    elif arg == 'write' or arg == 'w':
        shell.write():
    elif arg == 'mung' or arg == 'm':
        script.mung():
    elif arg == 'show' or arg == 's':
        show.show():
    elif arg == 'page' or arg == 'p':
        shell.page():
    elif arg == 'help' or help == 'h':
        help.help():
    else:
        print('No such command')
