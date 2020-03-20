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

context = Context("javascript")


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
        "code boo": "bool",
        "not equals undefined": " !== 'undefined'",
        # variables 
        "const": "const ",
        "static": "static ",
        # functions
        "state func": "function ",
        "state return": "return ",
        "state constructor": "constructor ",
        "state goto": "goto ",
        "state import": "import ",
        "state from": [" from '';", Key("left left")],
        "state class": "class ",
        "state extends": "extends ",
        "state super": "super();",
        "comment js": "// ",
        "refill asink": " async ",
        # console snippets
        "console log": ["console.log();", Key("left left")],
        "console error": ["console.error();", Key("left left")],
        "console warn": ["console.warn();", Key("left left")],
        # commands for react
        "refill import": "import React from 'react';",
        "refill in line": ["< />", Key("left left left")],
        "refill open": ["<>", Key("left")],
        "refill closed": ["</>", Key("left")],
        "refill clack": "onClick",
        "refill component": [" extends React.Component {}", Key("left enter enter up tab")],
        "refill simple component": [" extends React.Component {}", Key("left enter enter up tab")],
        "refill fragment": ["<React.Fragment></React.Fragment>", Key("escape b b b b a")],
        "refill simple fragment": ["<Fragment></Fragment>", Key("escape b b a")],
        "document render": ["ReactDOM.render()", Key("left")],
        "refill class name set": [" className={}", Key("left")],
        "refill class name import": "import classnames from 'classnames';",
        "refill prop types set": [".propTypes = {};", Key("left left enter enter up tab")],
        "refill prop types import": "import PropTypes from 'prop-types';",
    }
)
