from core.components import Components, Component
from core.events import Events
from core.interfaces.CursesIO import CursesIO

def on_start(**context):
    components : Components = context["components"]
    curses = CursesIO()
    curses.setup()
    io_store : Component = Component(0, "io", {"curses": curses})
    components.add(io_store)

def on_tick(**context):
    events : Events = context["events"]
    components : Components = context["components"]
    io : CursesIO = components.of_type("io")[0]["curses"]
    next_input = io.pop_input()
    while next_input != None:
        events.fire_event("input_received", text=next_input, **context)
        next_input = io.pop_input()
    io.poll()

def on_shutdown(**context):
    components : Components = context["components"]
    io : CursesIO = components.of_type("io")[0]["curses"]
    io.exit()

__register__ = [on_tick, on_start, on_shutdown]