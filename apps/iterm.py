from talon.voice import Key, Context

ctx = Context("iterm", bundle="com.googlecode.iterm2")

keymap = {
    "broadcaster": Key("cmd-alt-i"),
    "password": Key("cmd-alt-f"),
    # Pane creation and navigation
    "split horizontal": Key("cmd-shift-d"),
    "split vertical": Key("cmd-d"),
    "pane next": Key("cmd-]"),
    "pane last": Key("cmd-["),

    # Vim
    # editing
    "now save": Key("escape : w enter"),
    "now quit": Key("escape : q ! enter"),
    "new line": Key( "escape o" ),
    "new line up": Key( "escape O"),
    "paste line": Key("escape p"),
    "paste line up": Key("escape P"),
    "now undo": Key( "escape u"),
    "super undo": Key("ctrl-r"),
    "now (eye | before)": Key("escape i"),
    "now after": Key("escape a"),
    "add to start": Key("escape I"),
    "add to end": Key("escape A"),
    "change word": Key("escape d w i"),
    "delete word": Key("escape d w"),
    "delete line": Key("escape d d"),
    "delete rest": Key("escape D"),
    # navigating
    "( tarp | top | gg )": Key("g g"),
    "( bot | bottom | big G )": "G",
    "search": Key("escape /"),
    "(this | viz)": Key("escape v"),
    "now back": "B",
    "now backing": "b",
    "now foward": "W",
    "now flooring": "w",
    "now end": "E",
    "now ending": "e",
    "now start": "^",
    "now end": "$",
    "now last": Key("escape ` ."),
    "now copy": Key("c p"),
    # vim plugins
    "( prev | preev | previous | last) chunk": Key("[ c"),
    "next chunk": Key("] c"),
    "stage": Key("\\ h a"),
    "unstage": Key("\\ h r"),

    # Terminal
    "clear line": Key("ctrl-u"),
    "clear window": Key("cmd-k"),
    "now (end pee end | NPM )": "npm ",
    "now (end pee end | NPM ) run": "npm run ",
    "now (end pee end | NPM ) install": "npm install ",
    "now (vim | edit)": "vim ",
    "now (vim | edit) all": ["vim", Key("enter")],
    "now (at | act)": ['ack -i ""', Key("left")],
}

ctx.keymap(keymap)
