from core.context import Context
from core.components import Component, Components
from scripts.text_shared.contexts import OutputContext

def make_print(context : Context):
    return lambda output : context.events.fire_event("output", OutputContext(output, context))

def get_location(id : int, **context):
    pass

def get_objs_in_location(id : int, context : Context):
    locations = context.components.of_type("location")
    locations : list[Component] = list(filter(lambda loc : loc["id"] == id, locations))
    return [location.obj_id for location in locations]