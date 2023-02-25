from core.utility import get_generic_context

def make_print(**context):
    con = get_generic_context(context)
    events = context["events"]
    return lambda output : events.fire_event("output", output = output, **con)

def get_location(id : int, **context):
    pass