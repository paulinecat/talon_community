from talon.voice import Context, Key

ctx = Context("symbol")

keymap = {
    # simple
    "(question [mark] | questo)": "?",
    "plus": "+",
    "tilde": "~",
    "(bang | exclamation point | clamor)": "!",
    "(doll | dollar [sign] | dolly)": "$",
    "(under score | downscore | crunder)": "_",
    "(colon | cold | coal)": ":",
    "(lparen | [left] paren | precorp )": "(",
    "(rparen | are paren | right paren | precose)": ")",
    "(brace | left brace | kirksorp)": "{",
    "(rbrace | are brace | right brace | kirkos)": "}",
    "(angle | left angle | less than)": "<",
    "(rangle | are angle | right angle | greater than)": ">",
    "(star | asterisk)": "*",
    "(pound | hash [sign] | octo | number sign)": "#",
    "percent [sign]": "%",
    "caret": "^",
    "at sign": "@",
    "(and sign | ampersand | amper | amp)": "&",
    "(pipe | spike)": "|",
    "(dubquote | double quote | dub | dub dub)": '"',
    # compound
    "mintwice": "--",
    "plustwice": "++",
    "minquall": "-=",
    "pluqual": "+=",
    "starqual": "*=",
    "triple quote": "'''",
    "triple tick": "```",
    "[forward] dubslash": "//",
    "coal two": "::",
    "(dot dot | dotdot)": "..",
    "(ellipse | eclipse | ellipsis | dot dot dot | dotdotdot | triple dot)": "...",
    # unnecessary: use repetition commands?
}

ctx.keymap(keymap)
