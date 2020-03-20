"""
Commands that write bits of code that is valid for multiple languages
"""

from talon.voice import Context, Key

ctx = Context("general_lang")

ctx.keymap(
    {
        # Operators
        "(offer equals | assign | equeft)": " = ",
        "(offer (minus | subtract) | deminus)": " - ",
        "(offer (plus | add) | deplush)": " + ",
        "(offer (times | multiply) | duster)": " * ",
        "(offer divide | divy)": " / ",
        "offer mod": " % ",
        "((offer minus | subtract) equals | minus assign)": " -= ",
        "((offer plus | add) equals | (plus | add) assign)": " += ",
        "([offer] (times | multiply) (assign | equals) | star assign)": " *= ",
        "[offer] divide (assign | equals)": " /= ",
        "[offer] mod (assign | equals)": " %= ",
        "(offer colon (equals | assign) | coleek)": " := ",
        "(offer | is) greater [than]": " > ",
        "(offer | is) less [than]": " < ",
        "((offer | is) equal [to] | longqual)": " == ",
        "((offer | is) not equal [to] | banquall)": " != ",
        "((offer | is) greater [than] or equal [to] | grayqual)": " >= ",
        "((offer | is) less [than] or equal [to] | lessqual)": " <= ",
        "([(offer | is)] exactly (equal [to] | equals) | triple equals | trickle)": " === ",
        "([(offer | is)] not exactly (equal [to] | equals) | ranqual | nockle)": " !== ",
        "(offer (power | exponent) | to the power [of])": " ** ",
        "offer and": " && ",
        "offer or": " || ",
        "[offer] (logical | bitwise) and": " & ",
        "([offer] (logical | bitwise) or | (offer | D) pipe)": " | ",
        "[(offer | logical | bitwise)] (ex | exclusive) or": " ^ ",
        "(offer | logical | bitwise) (left shift | shift left)": " << ",
        "(offer | logical | bitwise) (right shift | shift right)": " >> ",
        "(offer | logical | bitwise) and equals": " &= ",
        "(offer | logical | bitwise) or equals": " |= ",
        "(offer | logical | bitwise) (ex | exclusive) or equals": " ^= ",
        "[(offer | logical | bitwise)] (left shift | shift left) equals": " <<= ",
        "[(offer | logical | bitwise)] (right shift | shift right) equals": " >>= ",
        "[offer] small (arrow | lambo)": " -> ",
        "[offer] (arrow | lambo)": " =>",
        # Empty
        "empty (parens | call | prexy)": "()",
        "empty (dict | object)": "{}",
        "empty (array | brackers)": "[]",
        # Inline
        "in line call": ["()", Key("left")],
        "in line hobby": ["{}", Key("left")],
        "in line array": ["[]", Key("left")],
        # Blocks
        "brace block": [" {}", Key("left enter enter up tab")],
        "brace next block": [Key("cmd-right enter"), "{}", Key("enter up right enter tab")],
         "(square | brax) block": ["[]", Key("left enter enter up tab")],
        "(paren | prex) block": ["()", Key("left enter enter up tab")],
        # Combos
        "coalshock": [":", Key("enter")],
        "comshock": [",", Key("enter")],
        "sinker": [Key("cmd-right ;")],
        "swipe": ", ",
        "coalgap": ": ",
        "[forward] slasher": "// ",
        # Statements
        "state (def | deaf | deft)": "def ",
        "state if": ["if ()", Key("left")],
        "state else if": [" else if ()", Key("left")],
        "state else": " else ",
        "state while": ["while ()", Key("left")],
        "state for": ["for ()", Key("left")],
        "state switch": ["switch ()", Key("left")],
        "state case": ["case \nbreak;", Key("up")],
        # Other Keywords
        "tip pent": "int ",
        "tip (char | care)": "char ",
        "tip byte": "byte ",
        "tip float": "float ",
        "tip double": "double ",
        "tip no": "null",
        "tip bully": "boolean",
        # Comments
        "comment see": "// ",
        "comment py": "# ",
        # Miscellaneous
        "code chase on": "json",
        "code (jsx | chase sx )": "jsx",
        "code chase": "js",
        "code pie" : "py",
        "code (sea assess | c s s)": "css",
    }
)
