from core.components import Components, Component
from scripts.text_shared.utility import make_print, get_objs_in_location
from core.interfaces.magic_io import COLOR, RichText
from core.context import Context
from scripts.text_shared.contexts import UseSkillContext

def on_start(context : Context):
    global pprint
    pprint = make_print(context)

def on_call(context : UseSkillContext):
    components : Components = context.components
    sender : int = context.source

    # Check if they have any location to look at.
    location = components.on_object(sender, "location")
    if len(location) == 0:
        pprint("You have no location. You can't see anything.")
        return
    location = location[0]

    room = components.on_object(location["id"], "descriptor")
    if len(room) == 0:
        return
    room = room[0]

    if len(context.args) == 0:
        # If no arguments, print description of room.
        pprint(RichText(room["name"], color=COLOR.YELLOW, bold=True))
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

    elif len(context.args) > 0:
        # If one or more args, print description of first object
        obj_name = context.args[0]
        objs_here = get_objs_in_location(room.obj_id, context)
        # objs_matching = []
        for obj in objs_here:
            descriptors = components.on_object(obj, "descriptor")
            if len(descriptors) > 0 and descriptors[0]["name"].lower() == obj_name.lower():
                pprint(RichText(descriptors[0]["name"], color=COLOR.YELLOW, bold=True))
                pprint(descriptors[0]["description"])
                return
        pprint(f"You can't see any {obj_name} here.")

__register__ = [on_start, on_call]