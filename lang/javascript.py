from talon.voice import Context, Key, press
import talon.clip as clip
from ..utils import (
    text,
    parse_words,
    parse_words_as_integer,
    insert,
    word,
    join_words,
    is_filetype,
)

JS_EXTENSIONS = (".js", ".jsx")

context = Context("javascript", func=is_filetype(JS_EXTENSIONS))


def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = " ".join(words)
    s = s.replace(" – ", "-")
    insert(s)


def CursorText(s):
    left, right = s.split("{.}", 1)
    return [left + right, Key(" ".join(["left"] * len(right)))]


context.keymap(
    {
        "tip bool": "bool",
        "not equals undefined": " !== 'undefined'",
        # variables 
        "const": "const ",
        "let": "let",
        "static": "static ",
        # functions
        "state func": "function ",
        "state return": "return ",
        "state constructor": "constructor ",
        "state goto": "goto ",
        "state import": "import ",
        "state from": ["from '';", Key("left left")],
        "state class": "class ",
        "state extends": "extends ",
        "state super": "super",
        "comment js": "// ",
        "asink": " async ",
        # console snippets
        "console log": ["console.log();", Key("left left")],
        "console error": ["console.error();", Key("left left")],
        "console warn": ["console.warn();", Key("left left")],
        # commands for react
        "react import": "import React from 'react';",
        "react tag": ["< />", Key("left left left")],
        "react clack": "onClick",
        "react component": ["React.Component ", Key("left")],
        "react fragment": ["React.Fragment ", Key("left")],
        "component": "Component",
        "fragment": "Fragment",
        "document render": ["ReactDOM.render()", Key("left")],
    }
)
