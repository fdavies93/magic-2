from core.utility import get_generic_context
from core.events import Events
from core.components import Components, Component
from core.interfaces.magic_io import *
from scripts.text_shared.utility import make_print
from scripts.text_shared.contexts import InputContext, UseSkillContext
from core.context import Context

# Important question (but doesn't need answering immediately):
# Should Parser be a class rather than a plain function?
# If so where should it be declared? In the core? As a demo script?
# As a core.utility class?
# I tend towards 'yes' for it being a class but am unclear on the
# second question. Minimalism implies even the parser should be a
# module.

def on_start(context : Context):
    context.events.add_trigger("input", "parser.parse")
    global pprint
    pprint = make_print(context)

def parse(context : InputContext):
    # ugly, ugly, ugly
    # this could all be one-liners if context were an ABC\
    split : str = context.text.split(" ")
    verb : str = split[0]
    con = UseSkillContext(context.source, verb, split[1:], context)
    fired = context.events.fire_event(f"attempt_{verb}", con)

    if not fired:
        pprint(f"I don't understand what {verb} means.")       

__register__ = [parse, on_start]