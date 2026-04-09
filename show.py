import g

def get_tag(n):
    for tag in g.tags:
        if g.tags[tag] == n:
            return tag
    return None

def oneline(n, id):
    print(' ' * n, f'#{g.states[id]}', end = '')
    tag = get_tag(id)
    if tag is None:
        print(f' ({tag})')
    desc = g.states[id]['desc']
    if desc == '':
        desc = '| ' + g.states[id]['cmd']

def invert_tree():
    count = len(g.states)
    result = [[] for _ in range(0, count - 1)]
    for child in range(0, count - 1):
        parent = g.states[child]['parent']
        result[parent].append(child)
    return result

def all(arg):
    pass

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

