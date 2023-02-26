from core.utility import get_generic_context
from core.events import Events
from core.components import Components, Component
from core.interfaces.magic_io import *
from scripts.utility import make_print

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
    components : Components = context["components"]
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

    # if split[0] == "look":
    #     location = components.on_object(sender, "location")
    #     if len(location) == 0:
    #         pprint("You have no location. You can't see anything.")
    #         return
    #     location = location[0]
    #     room = components.on_object(location["id"], "descriptor")
    #     if len(room) == 0:
    #         return
    #     room = room[0]
    #     pprint(RichText(room["name"], color=COLOR.YELLOW))
    #     pprint(room["description"])

    #     locations = components.of_type("location")
    #     locations : list[Component] = list(filter(lambda loc : loc["id"] == room.obj_id, locations))
    #     names = []
    #     for loc in locations:
    #         descs = components.on_object(loc.obj_id, "descriptor")
    #         if len(descs) == 0:
    #             continue
    #         names.append(descs[0]["name"])
    #     if len(names) > 0:
    #         pprint(f"You can see {', '.join(names)}.")        

__register__ = [parse, on_start]