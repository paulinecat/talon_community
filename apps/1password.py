# Talon voice commands for interacting with 1password
# John S. Cooper  jcooper@korgrd.com

from talon.voice import Key, Context

ctx = Context("1password", bundle="com.agilebits.onepassword4")

ctx.keymap(
    {
        "pass new": Key("shift-cmd-n"),
        "past duke": Key("cmd-d"),
        "pass edit": Key("cmd-e"),
        "pass copy": Key("shift-cmd-c"),
        "[show] next category": Key("cmd-}"),
        "[show] (preev | previous) category": Key("cmd-{"),
    }
)

global_password = Context("1password")
global_password.keymap({"pass fill": Key("shift-ctrl-alt-/")})
