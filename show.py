# Display the tree or a single node

import g

def get_tag(n):
    for tag in g.tags:
        if g.tags[tag] == n:
            return tag
    return None

def oneline(id, n):
    print(' ' * n, f'#{g.states[id]}', end = '')
    tag = get_tag(id)
    if tag is None:
        print(f' ({tag})', end='')
    desc = g.states[id]['desc']
    newline_pos = desc.find('\n')
    desc = desc[0:newline_pos]
    if desc == '':
        desc = '| ' + g.states[id]['cmd']
    print(' ', desc)

def invert_tree():
    count = len(g.states)
    result = [[] for _ in range(0, count)]
    for child in range(0, count - 1):
        parent = g.states[child]['parent']
        result[parent].append(child)
    return result

def recur(tree, id, depth):
    children = tree[id]
    if len(children) != 0:
        oneline(children[0], n)
        for child in children[1:-1]:
            oneline(child, n + 1)
            recur(tree, child, depth + 1)

def all(arg):
    tree = invert_tree()
    oneline(0, 0)
    recur(tree, 0, 0)

def show(arg):
    state = g.states[g.current]
    print(f'File: {g.pathname}')
    print(f'State #{g.current}:', end='')
    tag = get_tag(g.current)
    if tag is not None:
        print(f' (tag: {tag})')
    else:
        print()
    print(f'  Command: {state["cmd"]}')
    print('  Parent; ', end='')
    parent = state['parent']
    if parent is None:
        print('none')
    else:
        print(parent)
    print('  Dependencies: ', end='')
    deps = ', '.join(state['deps'])
    if deps == '':
        print('none')
    else:
        print(deps)
    desc = state['desc']
    if desc == '\n' or desc == '':
        print('  Description: none')
    else:
        print(f'  Description:\n{desc}')

