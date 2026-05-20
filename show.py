# Display the tree or a single node

import g


# Given a state number, return a tag
def get_tag(n):
    for tag in g.tags:
        if g.tags[tag] == n:
            return tag
    return None


# Print one line for "all" and "show" commands
# Shows the state number, tag, and first line of the description
# If there is no description, use the command;
# if there is no command, use "Edited" or "Read file".
# Returns the rest of the description
def print_one(id, depth):
    spaces = "  " * depth
    print(f'{spaces}#{id}', end='')
    tag = get_tag(id)
    if tag is not None:
        print(f':{tag}', end='')
    state = g.states[id]
    desc = state['desc']
    newline_pos = desc.find('\n')
    short_desc = desc[0:newline_pos]
    mode = state['mode']
    cmd = state['cmd']
    if short_desc != '':
        pass
    elif (mode == None):
        short_desc = 'initial state'
    elif mode == 'edit':
        short_desc = 'Edited'
    elif mode == 'file':
        short_desc = 'Read file:' + cmd
    elif mode == 'pipe':
        short_desc = 'Command: ' + cmd
    print(' ', short_desc)
    return desc[newline_pos+1:]


# Invert the tree of states
# Whereas g.states has each state holding its parent,
# the result of this function has each state holding its children.
def invert_tree():
    count = len(g.states)
    result = [[] for _ in range(0, count)]
    for child in range(1, count):
        parent = g.states[child]['parent']
        result[parent].append(child)
    return result


# Print the children (and their children, etc.) with proper indentation.
# Uses print_one to do the actual printing.
def print_subtree(tree, id, depth):
    print_one(id, depth)
    children = tree[id]
    for child_index in range(0, len(children)):
        child = children[child_index]
        print_subtree(tree, children[child_index], depth + 1)

# The 'all' command.
def all(_):
    tree = invert_tree()
    print(f'tree={tree}')
    print_subtree(tree, 0, 0)

def show(_):
    print(f'File: {g.pathname}')
    desc = print_one(g.current, 0)
    print(desc)
    print('Parent: ', end='')
    parent = g.states[g.current]['parent']
    if parent is None:
        print('none')
    else:
        print(parent)

