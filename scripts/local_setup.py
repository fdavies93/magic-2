from core.components import Component, Components

def on_start(**context):
    components : Components = context["components"]

    room_id = components.get_next_id()
    room_descriptor = Component(room_id, "descriptor", {"name": "A room.", "description": "This is a test description."})
    components.add(room_descriptor)

    player_id = components.get_next_id()
    player_input_source = Component(player_id, "input_source", {})
    player_descriptor = Component(player_id, "descriptor", {"name": "Player", "description": "You're looking very handsome."})
    player_location = Component(player_id, "location", {"id": room_id})
    components.add(player_input_source)
    components.add(player_descriptor)
    components.add(player_location)

__register__ = [on_start]