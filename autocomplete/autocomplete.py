#! /usr/bin/python

import readline

commands = [
    "eggs",
    "cheese",
    "bread",
    "five"
]

def completer(text, state):
    print "in completer"
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)
