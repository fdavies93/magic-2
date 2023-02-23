from core.events import Events
from core.components import Components, Component

def test_tick(**context):
    # print(f"Timestamp: {context['timestamp']}")
    components : Components = context["components"]
    bodies = components.of_type("physics_body")
    for body in bodies:
        pos = body["pos"]
        body["pos"] = (pos[0] + 10, pos[1] + 5)
        # print(f"Body with id {body.obj_id} now at position {pos}.")


def test_start(**context):
    components : Components = context["components"]
    print("Starting game!")
    for i in range(5):
        new_c = Component(components.get_next_id(), "physics_body", {"pos": (0, 0)})
        components.add(new_c)

__register__ = {
    # "on_tick": test_tick,
    "on_start": test_start
}