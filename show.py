# Display the tree or a single node

import g

# Print one line for "all" command
# Shows the state number, tag, and first line of the description
def oneline(id, n):
    print(f'#{id}', end='')
    tag = util.get_tag(id)
    if tag is not None:
        print(f' ({tag})', end='')
    state = g.states[id]
    desc = state['desc']
    newline_pos = desc.find('\n')
    desc = desc[0:newline_pos]
    if desc == '':
        mode = state['mode']
    print(' ', desc)

# Invert the tree of staes
# Whereas g.states has each state holding its parent,
# the result of this function has each state holding its children.
def invert_tree():
    count = len(g.states)
    result = [[] for _ in range(0, count)]
    for child in range(0, count - 1):
        parent = g.states[child]['parent']
        result[parent].append(child)
    return result

# Print the children (and their children, etc.) with proper indentation.
# Uses oneline to do the actual printing.
def recur(tree, id, depth):
    children = tree[id]
    if len(children) != 0:
        oneline(children[0], n)
        for child in children[1:-1]:
            oneline(child, n + 1)
            recur(tree, child, depth + 1)

# The 'all' command.
def all(_):
    tree = invert_tree()
    oneline(0, 0)
    recur(tree, 0, 0)

def show(_):
    state = g.states[g.current]
    print(f'File: {g.pathname}')
    print(f'State #{g.current}:', end='')
    tag = util.get_tag(g.current)
    if tag is not None:
        print(f' (tag: {tag})')
    else:
        print()
    mode = state['mode']
    if mode is None:
        pass
    elif mode == 'pipe':
        print('  Command: ', end='')
        cmd = state['cmd']
        if cmd is None:
            print('none')
        else:
            print(cmd)
    elif mode == 'edit':
        print(  'Edited')
    elif mode == 'read':
        readfile = g.states[g.current]['cmd']
        print(f'  Read file: {readfile}')
    print('  Parent: ', end='')
    parent = state['parent']
    if parent is None:
        print('none')
    else:
        print(parent)
    deps = ', '.join(state['deps'])
    if deps != '':
        print('  Dependencies: {deps} ', end='')
    desc = state['desc']
    if desc == '\n' or desc == '':
        print('  Description: none')
    else:
        print(f'  Description:\n{desc}')

