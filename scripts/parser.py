from core.utility import get_generic_context
from core.events import Events
from core.components import Components, Component
from core.interfaces.magic_io import *

def on_start(**context):
    events : Events = context["events"]
    events.add_trigger("input", "parser.parse")

def parse(**context):
    components : Components = context["components"]
    generic_context = get_generic_context(context)
    events : Events = context["events"]
    input : str = context["text"]
    sender : str  = context["source"]
    # events.fire_event("output", output = f"Received input from object id {sender}", **generic_context)

    if input == "look":
        location = components.on_object(sender, "location")
        if len(location) == 0:
            events.fire_event("output", output = "You have no location. You can't see anything.", **generic_context)
            return
        location = location[0]
        room = components.on_object(location["id"], "descriptor")
        if len(room) == 0:
            return
        room = room[0]
        events.fire_event("output", output = RichText(room["name"], color=COLOR.YELLOW), **generic_context)
        events.fire_event("output", output = room["description"], **generic_context)

__register__ = [parse, on_start]