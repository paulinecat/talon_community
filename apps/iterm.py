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

    # Vim commands
    "save it": Key("escape : w enter"),
    "new [(lie | line)]": Key( "escape o" ),
    "new up [(lie | line)]": Key( "escape O"),
    "undo": Key( "escape u"),
    "super undo": Key("ctrl-r"),
    "(eye | before)": Key("escape i"),
    "after": Key("escape a"),
    "say eye": Key("escape I"),
    "say ay": Key("escape A"),
    "change [word]": Key("escape d w i"),
    "delete word": Key("escape d w"),
    "delete line": Key("escape d d"),
    "delete rest": Key("escape D"),
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
    "start": "^",
    "end": "$",
    "last": Key("escape ` ."),
    "copy": Key("c p"),
    "( prev | preev | previous | last) chunk": Key("[ c"),
    "next chunk": Key("] c"),
    "stage": Key("\\ h a"),
    "unstage": Key("\\ h r"),
    "[quit] out": Key("escape : q ! enter"),
    "paste": Key("escape p"),
    "paste up": Key("escape P"),
    
    # Terminal
    "clear line": Key("ctrl-u"),
    "now (end pee end | NPM )": "npm ",
    "now (end pee end | NPM ) run": "npm run ",
    "now (end pee end | NPM ) install": "npm install ",
}

ctx.keymap(keymap)
