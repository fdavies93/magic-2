from core.context import Context
from core.events import Events
from core.components import Components, Component

def test_tick(**kwargs):
    context : Context = kwargs["context"]
    print(f"Timestamp: {kwargs['timestamp']}")
    components = context.components
    bodies = components.of_type("physics_body")
    for body in bodies:
        pos = body.data["pos"]
        body.data["pos"] = (pos[0] + 10, pos[1] + 5)
        print(f"Body with id {body.obj_id} now at position {pos}.")


def test_start(**kwargs):
    context : Context = kwargs["context"]
    components = context.components
    print("Starting game!")
    for i in range(5):
        new_c = Component(i, "physics_body", {"pos": (0, 0)})
        components.add(new_c)

__register__ = {
    "on_tick": test_tick,
    "on_start": test_start
}