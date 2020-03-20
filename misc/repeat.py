#     {
        # "wink": Rep(1),
        # "creek": RepPhrase(1),
        # "soup": Rep(1),
        # "trace": Rep(2),
        # "core": Rep(3),
        # "fights": Rep(4),
        # "(repeat | repple)" + utils.numerals: repeat,
#     }

from talon.voice import Context, Rep, talon, generic
from ..utils import parse_words_as_integer

class MyRep(generic):
    def __call__(self, m):
        tmp = []
        if self.ctx.last_action:
            for action, rule in self.ctx.last_action:
                for i in range(self.data):
                    act = action(rule) or (action, rule)
                tmp.append(act)
        return tmp

# use this if you want `action trace` to result in action being executed 3 times
offset = -1
# use this if you want `action` pause `trace` to result in action being executed 4 times
# offset = 0

ctx = Context('repeater')

def repeat(m):
    repeat_count = parse_words_as_integer(m._words[1:])

    if repeat_count != None and repeat_count >= 1:
        repeater = MyRep(repeat_count)
        repeater.ctx = talon
        return repeater(None)

def test(m):
    test = parse_words_as_integer(m._words[1:])
    print(test)

ctx.keymap({
    'wink': MyRep(1),
    'soup': MyRep(2),
    'trace': MyRep(3),
    'core': MyRep(4),
    'fights': MyRep(5),
    'repeat (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)++': repeat,
    'hagrid (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)++': test
})
