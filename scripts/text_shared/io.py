from core.components import Components, Component
from core.events import Events
from core.interfaces.CursesIO import CursesIO
from core.context import Context, TickContext
from scripts.text_shared.contexts import InputContext, OutputContext

def on_start(context : Context):
    global curses
    curses = CursesIO()
    curses.setup()
    context.events.add_trigger("output","io.output")

def on_tick(context : TickContext):
    sources = context.components.of_type("input_source")
    next_input = curses.pop_input()
    while next_input != None:
        for input_source in sources:
            context.events.fire_event("input", InputContext(input_source.obj_id, next_input, context.make_generic()))
        next_input = curses.pop_input()
    curses.poll()

def output(context : OutputContext):
    curses.add_output(context.output)

def on_shutdown(context : Context):
    curses.exit()

__register__ = [on_tick, on_start, on_shutdown, output]