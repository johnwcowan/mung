import os
# Display help for all commands plus help for each command

import g

def help_main():
    os.system(f"""{g.pager} <<END
Editing commands:
|               filter state to make new state
describe / d    set description for state
edit / e        edit state into a new state

State tree commands:
all / a         show whole tree
undo / u        undo last change to state
Tag commands:
tag / t         tag current state with specified tag
jump / j        jump to specified tagged state
back / b        return from last jump or undo

Termination commands:
destroy         destroy the history and terminate
quit / q / EOF  just terminate

I/O commands:
read / r        read specified file to get the next state
write / w       write current state to specified file
mung / m        write script to get to current state to specified file

Miscellaneous commands:
show / s        file and state metadata
page / p        view current state with pager
help / h        show this help
!               run shell command (backslash for multiline command)
END """)

def help_pipe():
    print("""\
Specify a shell command that filters the current state to produce a new
state, and make the new state current.  If a line ends in backslash,
prompt for more lines until a line not ending in a backslash is read.
Text within braces represents the number or tag of a state:
it is converted into the name of the file holding that state.""")

def help_describe():
    print("""\
Specify a description of the current state.  If a line ends in backslash,
prompt for more lines until a line not ending in a backslash is read.""")

def help_edit():
   print(f"""\
Run {g.editor} to edit the current state to produce a new state, and
make the new state current.""")

def help_all():
    print("""\
Display all the states.""")

def help_undo():
    print("""\
Switch to the state from which the current state was created.""")


def help_tag():
    print("""\
Specify a tag that identifies the current state. If another
state has that tag, it is revoked.""")

def help_jump():
    print("""\
Switch to the state identified by number or tag.""")

def help_back():
    print("""\
Return to the state from which the last jump or undo command was issued.""")

def help_destroy():
    print("""\
Destroy the history and terminate mung.  If the current state has not
been written, this command must be given twice in a row to prevent
unintentional loss.""")

def help_quit():
    print("""\
Terminate mung, preserving the history.""")

def help_read():
    print("""\
Create a new state with the contents of the specified file, and make it
current. The content of the current state is not used.""")

def help_write():
    print("""\
Write the contents of the current state to the specified file:
the default is the original file being munged.""")

def help_mung():
    print("""\
Write a script of shell commands that when executed will transform
the standard input and write the result to the standard output, after
performing all the steps specified by | commands, edit commands, and read
commands to get there.  Note that the editor will be run and the user
must repeat whatever was originally done in it to get to the next state.
Read commands will take their input from the originally named file.""")

def help_show():
    print("""\
Display information about the file being munged and the current state.""")

def help_page():
    print("""\
View the contents of the current state using the specified pager.
The pager should not make any changes to the state.  The default pager
is {g.pager}.""")

def help_cat():
    print("""\
Send the contents of the current state to the standard output""")

def help_help():
    print("""\
Display the list of commands and a brief explanation of each.
If a command is specified, give help on that command.""")

def help_bang():
    print("""\
Execute the specified shell command. This has no effect on the current
state or the history.  If the command ends in backslash, prompt for
more lines until a line not ending in a backslash is read.""")

def help(cmd):
    if cmd is None:
        help_main();
    elif cmd == '|':
        help_pipe()
    elif cmd == 'describe' or cmd == 'd':
        help_describe()
    elif cmd == 'edit' or cmd == 'e':
        help_edit()
    elif cmd  == 'all' or cmd == 'a':
        help_all()
    elif cmd == 'undo' or cmd == 'u':
        help_undo()
    elif cmd == 'tag' or cmd == 't':
        help_tag()
    elif cmd == 'jump' or cmd == 'j':
        help_jump()
    elif cmd == 'back' or cmd == 'b':
        help_back()
    elif cmd == 'destroy':
        help_destroy()
    elif cmd == 'quit' or cmd == 'q':
        help_quit()
    elif cmd == 'read' or cmd == 'r':
        help_read()
    elif cmd == 'write' or cmd == 'w':
        help_write()
    elif cmd == 'mung' or cmd == 'm':
        help_mung()
    elif cmd == 'show' or cmd == 's':
        help_show()
    elif cmd == 'page' or cmd == 'p':
        help_page()
    elif cmd == 'help' or cmd == 'h':
        help_help()
    elif cmd == '!':
        help_bang()
    else:
        print(f'No help for {cmd}')
