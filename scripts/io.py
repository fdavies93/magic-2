from core.components import Components, Component
from core.events import Events
from core.interfaces.CursesIO import CursesIO

def on_start(**context):
    components : Components = context["components"]
    events : Events = context["events"]
    curses = CursesIO()
    curses.setup()
    io_store : Component = Component(components.get_next_id(), "io", {"curses": curses})
    components.add(io_store)
    events.add_trigger("output","io.output")

def on_tick(**context):
    events : Events = context["events"]
    components : Components = context["components"]
    sources = components.of_type("input_source")
    io : CursesIO = components.of_type("io")[0]["curses"]
    next_input = io.pop_input()
    while next_input != None:
        for input_source in sources:
            events.fire_event("input", source=input_source.obj_id, text=next_input, **context)
        next_input = io.pop_input()
    io.poll()

def output(**context):
    components : Components = context["components"]
    io : CursesIO = components.of_type("io")[0]["curses"]
    io.add_output(context["output"])

def on_shutdown(**context):
    components : Components = context["components"]
    io : CursesIO = components.of_type("io")[0]["curses"]
    io.exit()

__register__ = [on_tick, on_start, on_shutdown, output]