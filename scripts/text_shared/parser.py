from core.utility import get_generic_context
from core.events import Events
from core.components import Components, Component
from core.interfaces.magic_io import *
from scripts.text_shared.utility import make_print

# Important question (but doesn't need answering immediately):
# Should Parser be a class rather than a plain function?
# If so where should it be declared? In the core? As a demo script?
# As a core.utility class?
# I tend towards 'yes' for it being a class but am unclear on the
# second question. Minimalism implies even the parser should be a
# module.

def on_start(**context):
    events : Events = context["events"]
    events.add_trigger("input", "parser.parse")
    global pprint
    pprint = make_print(**context)

def parse(**context):
    # ugly, ugly, ugly
    # this could all be one-liners if context were an ABC
    input : str = context["text"]
    sender : str  = context["source"]
    ev : Events = context["events"]
    split : str = input.split(" ")
    verb : str = split[0]
    con = get_generic_context(context)
    con["verb"] = verb
    con["args"] = split[1:]
    con["sender"] = sender
    fired = ev.fire_event(f"attempt_{verb}", **con)

    if not fired:
        pprint(f"I don't understand what {verb} means.")       

__register__ = [parse, on_start]