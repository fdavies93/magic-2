from core.components import Component, Components
from core.utility import get_generic_context

def make_print(**context):
    con = get_generic_context(context)
    events = context["events"]
    return lambda output : events.fire_event("output", output = output, **con)

def get_location(id : int, **context):
    pass

def get_objs_in_location(id : int, **context):
    components : Components = context["components"]
    locations = components.of_type("location")
    locations : list[Component] = list(filter(lambda loc : loc["id"] == id, locations))
    return [location.obj_id for location in locations]