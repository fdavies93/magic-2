from core.components import Components, Component
from scripts.utility import make_print
from core.interfaces.magic_io import COLOR, RichText

def on_start(**context):
    global pprint
    pprint = make_print(**context)

def on_call(**context):
    components : Components = context["components"]
    sender : int = context["sender"]

    location = components.on_object(sender, "location")
    if len(location) == 0:
        pprint("You have no location. You can't see anything.")
        return
    location = location[0]
    room = components.on_object(location["id"], "descriptor")
    if len(room) == 0:
        return
    room = room[0]
    pprint(RichText(room["name"], color=COLOR.YELLOW))
    pprint(room["description"])

    locations = components.of_type("location")
    locations : list[Component] = list(filter(lambda loc : loc["id"] == room.obj_id, locations))
    names = []
    for loc in locations:
        descs = components.on_object(loc.obj_id, "descriptor")
        if len(descs) == 0:
            continue
        names.append(descs[0]["name"])
    if len(names) > 0:
        pprint(f"You can see {', '.join(names)}.")        

__register__ = [on_start, on_call]