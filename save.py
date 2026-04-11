# Loading and saving states

# Save the current state tp the history directory
def save():
    whole = {
        'states' : g.states,
        'tags' : g.tags,
        'stack' : g.stack,
    }
    with open(os.path.join(g.history_dir, 'pathname'), 'w') as file:
        print(g.pathname, file=file)
    with open(os.path.join(g.history_dir, 'state.json'), 'w') as file:
        json.dump(whole, file, ensure_ascii=False, indent=2)
        print(file=file)
    with open(os.path.join(g.history_dir, 'current'), 'w') as file:
        print(g.current, file=file)


