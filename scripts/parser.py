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
    split : str = input.split(" ")

    if split[0] == "look":
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

        locations = components.of_type("location")
        locations : list[Component] = list(filter(lambda loc : loc["id"] == room.obj_id, locations))
        names = []
        for loc in locations:
            descs = components.on_object(loc.obj_id, "descriptor")
            if len(descs) == 0:
                continue
            names.append(descs[0]["name"])
        if len(names) > 0:
            events.fire_event("output", output = f"You can see {', '.join(names)}.", **generic_context)        

__register__ = [parse, on_start]