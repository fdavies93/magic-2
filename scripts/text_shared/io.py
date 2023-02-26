from core.components import Components, Component
from core.events import Events
from core.interfaces.CursesIO import CursesIO

def on_start(**context):
    events : Events = context["events"]
    global curses
    curses = CursesIO()
    curses.setup()
    events.add_trigger("output","io.output")

def on_tick(**context):
    events : Events = context["events"]
    components : Components = context["components"]
    sources = components.of_type("input_source")
    next_input = curses.pop_input()
    while next_input != None:
        for input_source in sources:
            events.fire_event("input", source=input_source.obj_id, text=next_input, **context)
        next_input = curses.pop_input()
    curses.poll()

def output(**context):
    curses.add_output(context["output"])

def on_shutdown(**context):
    curses.exit()

__register__ = [on_tick, on_start, on_shutdown, output]